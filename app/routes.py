from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    #return "Hello, World!"
    user = {'username': 'geer'}
    return render_template('welcome.html')