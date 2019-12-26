from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/hello/<na>")
def hello(na):
    return "<h1>Hello {}</h1>" .format(na)


@app.route("/admin/")
def admin():
    return "<h1> Admin </h1>"


@app.route("/user/<name>")
def user(name):
    if name == "admin":
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('hello', na=name))
    

@app.route("/google")
def google():
    return redirect("http://google.com")


if __name__ == '__main__':
    app.run(debug=True)
