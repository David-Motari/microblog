from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'David'}
    posts = [
        {
           'author': { 'username': 'David'},
           'body': 'A beautiful day in Sobea'
        },
        {
           'author': { 'username': 'Davin'},
           'body': 'A beautiful day in Ngata'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
