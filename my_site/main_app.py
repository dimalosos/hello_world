
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

# create app object

app = Flask(__name__, template_folder='.')


# Configure
app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)

# Import blueprnts from controllers

from controllers.user import (
		user_blueprint, 
		#admin_blueprint,
)

# register Blueprints

app.register_blueprint(user_blueprint)

#app.register_blueprint(admin_blueprint)
