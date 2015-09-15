from flask import Flask, render_template, redirect, url_for, request
from jinja2 import Template
app = Flask(__name__, template_folder='.')

@app.route('/')
def home():
	return "Hello world"

@app.route('/users', methods = ['GET'])
def users():
		user = {
			'name': 'John',
			'email': 'johnny@gmail.com',
		}
		return render_template(
			'users.html', 
			title='Users',
			user=user,
			view_data={'user': user, 'user_friends': ['Bob', 'Alice']}
		)


if __name__ == '__main__':
	app.run(debug=True)


