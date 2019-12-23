<<<<<<< HEAD
from flask import render_template
from app import app

@app.route("/index/")
@app.route("/")
def index():
	return render_template('index.html')

@app.route("/login")
def login():
	return render_template('base.html')



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
=======
from app import app


@app.route("/")
def index():
	return "Hello Word 2"
>>>>>>> 4ece540f7f1b0317cab9880a0f37eacf8c1344a6
