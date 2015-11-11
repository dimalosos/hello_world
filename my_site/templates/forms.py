from flask_wtf import Form
from wtforms import TextField 
from wtforms.validators import DataRequired, Email


class UserForm(Form):
	username = TextField('username', validators=[DataRequired()])
	email = TextField('email', validators=[Email(message='Please write user\'s email')])
	