from wtforms import Form, BooleanField, TextField, PasswordField, validators

class UserForm(Form):
    username = TextField('username', [validators.Length(min=4, max=25)])
    email = TextField('email', [validators.Length(min=6, max=35)])