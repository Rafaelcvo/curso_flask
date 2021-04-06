from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/<int:id>')
def pessoa(id):
    soma = id + 1
    return jsonify({'id':soma, 'nome':'Rafael', 'profissao':'desenvolvedor'})

# @app.route('/soma/<int:valor1>/<int:valor2>/')
# def soma(valor1, valor2):
#     return jsonify({'soma': valor1 + valor2})

@app.route('/soma', methods=['POST'])
def soma():
    dados = json.loads(request.data)
    total = sum(dados['valores'])
    return jsonify({'soma':total})

if __name__ == '__main__':
    app.run(debug=True)
