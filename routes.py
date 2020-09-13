from flask import render_template, url_for
from app import app

@app.route('/')
def index():
    return "Hello, User!"

@app.route('/site1')
def site1():
    return "Site 1"

@app.route('/site2')
def site2():
    return "Site 2"

@app.route('/boiler')
def boiler():
        return render_template('boiler.html')

