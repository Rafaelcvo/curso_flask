# Aula 1

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Index 2"


if __name__ == '__main__':
    app.run()

