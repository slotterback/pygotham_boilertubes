from flask import render_template, url_for, redirect, request
from app import app, db
from models import Boiler, BoilerTube, TubePlugEvent

@app.route('/')
def index():
    return "Hello, User!"

@app.route('/boiler/<int:id>')
def boiler(id):
    boiler = Boiler.query.filter_by(id=id).first_or_404()
    return render_template('boiler_view.html', boiler=boiler)

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
    return render_template('boiler.html',boiler=boiler)

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
        return redirect(url_for('boiler',id))
    return render_template('boiler.html',boiler=boiler)


