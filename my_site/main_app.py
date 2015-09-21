import os
from json import dumps, loads
from flask import Flask, render_template, redirect, url_for, request
from flask import jsonify
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='.')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

from user import User

DB = './my_super_database.db'

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
    with open(DB, 'r') as f:
        users = loads(f.read() or '[]')
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
    # _create_db_if_doesnt_exist()
    # users_json = _read_users_from_db()
    # users_json = _append_user_to_json_list(users_json)
    # _write_users_to_db(users_json)
    return redirect(url_for('show_users'))

def _append_user_to_json_list(users_json):
    users = loads(users_json)
    users.append({
        'name': request.form['name'],
        'email': request.form['email'],
    })
    return dumps(users)

def _read_users_from_db():
    with open(DB, 'r') as f:
        return f.read() or '[]'

def _write_users_to_db(users_json):
    with open(DB, 'w') as f:
        f.write(users_json)

def _create_db_if_doesnt_exist():
    with open(DB, 'a') as f:
        pass
