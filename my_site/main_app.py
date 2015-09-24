import os
from flask import Flask, render_template, redirect, url_for, request
from flask.ext.sqlalchemy import SQLAlchemy



app = Flask(__name__, template_folder='.')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

from user import User



@app.route('/')
def home():
    return "Hello world"


@app.route('/users', methods = ['GET'])
def show_users():
    users = User.query.all()
    return render_template(
        'users.html', 
        title='Users',
        view_data={'users': users, 'user_friends': ['Bob', 'Alice']}
    )

@app.route('/users/create', methods = ['GET', 'POST'])
def create_user():
    if request.method == 'GET':
        return render_template('user_form.html')
    return _create_user()

def _create_user():
    user = User(request.form['name'], request.form['email'])
    db.session.add(user)
    db.session.commit()
    
    return redirect(url_for('show_users'))
