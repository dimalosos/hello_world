

import os

# zachem zdes os? gde my k nemu obrashaemsya?

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

# create app object

app = Flask(__name__, template_folder='.')

# config db 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

# Import blueprnts from controllers

from controllers.user import user_blueprint as user_blueprint

# register Blueprints

app.register_blueprint(user_blueprint)



