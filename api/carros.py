from flask import Blueprint, request, jsonify, make_response
from bd import Carros

carros_bp = Blueprint('carros', __name__)

@carros_bp.route('/carros', methods=['GET'])
def get_carros():
    return make_response(
        jsonify(
            message="Carros recuperados com sucesso!",
            data=Carros
        )
    )

@carros_bp.route('/carros', methods=['POST'])
def create_carro():
    carro = request.get_json()
    Carros.append(carro)

    return make_response(
        jsonify(
            message="Carro criado com sucesso!",
            data=carro
        )
    )

@carros_bp.route('/carros/<int:carro_id>', methods=['PUT'])
def edit_carro(carro_id):
    carro_novo = request.get_json()

    for carro in Carros:
        if carro['id'] == carro_id:
            carro.update(carro_novo)
            return make_response(
                jsonify(
                    message=f"Carro com ID {carro_id} editado com sucesso!",
                    data=carro
                )
            )

    return make_response(
        jsonify(
            message=f"Carro com ID {carro_id} não encontrado.",
            data=None
        ),
        404  # Código de resposta HTTP 404 Not Found
    )

@carros_bp.route('/carros/<int:carro_id>', methods=['DELETE'])
def delete_carro(carro_id):
    for index, carro in enumerate(Carros):
        if carro['id'] == carro_id:
            del Carros[index]
            return make_response(
                jsonify(
                    message=f"Carro com ID {carro_id} removido com sucesso!",
                )
            )

    return make_response(
        jsonify(
            message=f"Carro com ID {carro_id} não encontrado.",
            data=None
        ),
        404  # Código de resposta HTTP 404 Not Found
    )
