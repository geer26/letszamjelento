from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'geer'}
    return render_template('welcome.html')