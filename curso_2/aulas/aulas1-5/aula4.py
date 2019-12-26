from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/hello/")
def hello():
    return "<h1>Hello</h1>"


@app.route("/admin/<int:postID>")
def admin(postID):
    if postID >=1:
        return "<h1> Admin {}</h1>" .format(postID)
    else:
        return "<h1>Teste</h1>"


if __name__ == '__main__':
    app.run(debug=True)
