from flask import render_template, url_for, redirect, request
from marshmallow import ValidationError
from app import app, db
from models import Boiler, BoilerTube, TubePlugEvent
from schema import boiler_schema, boilers_schema, boiler_with_events_schema

### Main views

@app.route('/')
def index():
    boiler_ids = db.session.query(Boiler.id).all()
    return render_template('index.html',boiler_ids=boiler_ids,
                          subtitle="Select a Boiler")

@app.route('/boiler/<int:id>')
def boiler(id):
    boiler = Boiler.query.filter_by(id=id).first_or_404()
    return render_template('boiler_view.html', boiler=boiler,
                           subtitle="Current Boiler Status")

@app.route('/boiler_plug/<int:id>', methods=['GET', 'POST'])
def boiler_plug(id):
    boiler = Boiler.query.filter_by(id=id).first_or_404()
    if request.method == 'POST':
        for tube in boiler.tubes:
            if (request.form.get(f'tube{tube.id}')):
                tube.is_plugged = True
                e = TubePlugEvent(is_plug_event = True)
                tube.events.append(e)
        db.session.commit()
        return redirect(url_for('boiler',id=id))
    return render_template('boiler.html',boiler=boiler,
                           subtitle="Click on Tubes That Were Plugged")

@app.route('/boiler_repair/<int:id>', methods=['GET', 'POST'])
def boiler_repair(id):
    boiler = Boiler.query.filter_by(id=id).first_or_404()
    if request.method == 'POST':
        for tube in boiler.tubes:
            if (request.form.get(f'tube{tube.id}')):
                tube.is_plugged = False
                e = TubePlugEvent(is_plug_event = False)
                tube.events.append(e)
        db.session.commit()
        return redirect(url_for('boiler',id=id))
    return render_template('boiler.html',boiler=boiler,
                           subtitle="Click on Tubes That Were Replaced")

## API Views: Create
@app.route('/api/new_boiler', methods=['POST'])
def new_boiler():
    boiler=boiler_schema.load( request.get_json() )
    db.session.add( boiler )
    db.session.commit()
    print(boiler)
    return boiler_schema.dump( boiler )
        
### API Views: Read
@app.route('/api/get_boiler/<int:id>', methods=['GET'])
def get_boiler(id):
    boiler = Boiler.query.filter_by(id=id).first_or_404()
    return boiler_schema.dump(boiler)

@app.route('/api/get_boilers', methods=['GET'])
def get_boilers():
    all_boilers = Boiler.query.all()
    return boilers_schema.dump(all_boilers)

@app.route('/api/get_boiler_history/<int:id>', methods=['GET'])
def get_boiler_history(id):
    boiler = Boiler.query.filter_by(id=id).first_or_404()
    return boiler_with_events_schema.dump(boiler)

### API Views: Update
@app.route('/api/update_boiler/<int:id>', methods=['PUT'])
def update_boiler(id):
    pass

### API Views: Delete
@app.route('/api/remove_boiler/<int:id>', methods=['DELETE'])
def remove_boiler(id):
    boiler = Boiler.query.filter_by(id=id).first_or_404()
    db.session.delete(boiler)
    db.session.commit()
    return boiler_schema.dump(boiler)

