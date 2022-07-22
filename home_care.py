from flask import jsonify, Request, request
from flask import Flask
import uuid

app = Flask(__name__)

Paciente = []

@app.route("/cadastrar/pacientes", methods=['POST'])
def cadastro_paciente():
    registro = request.json 
    for listar in Paciente:
        if listar["cpf"] == registro["cpf"]:  
            return {"Algo deu errado.":"Esse cpf ja existe."}
    registro = {
        "id": str(uuid.uuid4()),
        "cpf": registro["cpf"],
        "senha": registro["senha"]
        }
    Paciente.append(registro)
    return jsonify(registro)