from flask import render_template
from app import app
from app.models.forms import LoginForm


@app.route("/index/")
@app.route("/")
def index():
	return render_template('index.html')

@app.route("/login")
def login():
	form = LoginForm()
	return render_template('login.html', form=form)



	# @app.route("/base/<user>")
	# @app.route("/base/", defaults={"user":None})
	# def base(user):
	# 	return render_template('base.html', user=user)

	#
	# @app.route("/test", defaults={'name':None})
	# @app.route("/test/", defaults={'name':None})
	# @app.route("/test/<name>")
	# def test(name):
	# 	if name:
	# 		return "Olá %s!" % name
	# 	else:
	# 		return "Olá usuario!"
from app import app

@app.route("/")
def index():
	return "Hello Word 2"
