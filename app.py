from flask import Flask, make_response, jsonify, request
from bd import Carros

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route("/carros", methods=["GET"])
def get_carros():
    return make_response(
        jsonify(
            message="Carros recuperados com sucesso!",
            data=Carros
        )
    )

@app.route('/carros', methods=['POST'])
def create_carro():
    carro = request.get_json()
    Carros.append(carro)

    return make_response(
        jsonify(
            message="Carro criado com sucesso!",
            data=carro
        )
    )

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"