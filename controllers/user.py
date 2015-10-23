# import flask dependencies

from flask import Flask, render_template, redirect, url_for, request, Blueprint

# From main app import db object

from my_site.main_app import db  

# From models import class User

from models.user import User

# Define a Blueprint for /user

user_blueprint = Blueprint('user', __name__,
                        template_folder='templates')

@user_blueprint.route('/')
def home():
    return reder_template(
        'templates/hello_world.html')


@user_blueprint.route('/users', methods = ['GET'])
def show_users():
    users = User.query.all()
    return render_template(
        'templates/users.html', 
        title='Users',
        view_data={'users': users, 'user_friends': ['Bob', 'Alice']}
    )

@user_blueprint.route('/users/create', methods = ['GET', 'POST'])
def create_user():
    if request.method == 'GET':
        return render_template('templates/user_form.html')
    return _create_user()

def _create_user():
    user = User(request.form['name'], request.form['email'])
    db.session.add(user)
    db.session.commit()
    
    return redirect(url_for('show_users'))