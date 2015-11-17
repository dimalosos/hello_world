from wtforms import (
	Form,
	TextField,
	PasswordField,
	validators,

)

class UserForm(Form):
    username = TextField('username', [validators.Length(min=4, max=25)])
    email = TextField('email', [validators.Email("e-mail goes here")])