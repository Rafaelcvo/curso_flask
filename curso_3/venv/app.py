from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello tword!"

def teste2():
    return "testes"

app.add_url_rule("/teste2", "teste2", teste2)


if __name__ == "__main__":
    app.run(debug=True)