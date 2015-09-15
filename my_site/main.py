from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__, template_folder='.')

@app.route('/')
def home():
	return "Hello world"

@app.route('/users', methods = ['GET'])
def users():
		return render_template('users.html')


if __name__ == '__main__':
	app.run(debug=True)


