from flask import Flask, redirect, url_for, request
from json import dumps

app = Flask(__name__, static_folder='public')


@app.route('/add', methods=["GET", "POST"])
def add():
    if request.method == "POST":
        return dumps(request.form)
    return "Ok Get"


if __name__ == '__main__':
    app.run(debug=True)
