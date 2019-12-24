from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/hello/")
@app.route("/hello/<name>")
def hello(name="visitante"):
    return "Ola {}".format(name)


@app.route("/admin/")
def admin():
    return "<h1> Admin </h1>"


if __name__ == '__main__':
    app.run(debug=True)
