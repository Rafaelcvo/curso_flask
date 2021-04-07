from flask import Flask, jsonify, request
import  json

app = Flask(__name__)

desenvolvedores = [
    {'nome':'Rafael',
     'habilidades':['Python', 'Java']},
    {'nome':'Gabriel',
     'habilidades':['Django', 'Flask']}
]

# Devolve um desenvolvedor pelo ID.

@app.route('/dev/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não exite.'.format(id)
            response = {'status':'erro', 'mensagem':mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'Sucesso', 'mesagem':'Registro excluido!'})

# Lista todos os desenvolvedores.
@app.route('/dev/')
def lista_desenvolvedores():


if __name__ == '__main__':
    app.run(debug=True)