from flask import jsonify, Request, request
from flask import Flask
import uuid

app = Flask(__name__)

Paciente = []

@app.route("/cadastrar/pacientes", methods=['POST'])
def cadastro_paciente():
    cadastro_pacientes = request.json 
    for listar in Paciente:
        if listar["cpf"] == cadastro_pacientes["cpf"]:  
            return {"Erro.":"Esse cpf ja existe."}
    cadastro_pacientes = {
        "id": str(uuid.uuid4()),
        "cpf": cadastro_pacientes["cpf"],
        "senha": cadastro_pacientes["senha"]
        }
    Paciente.append(cadastro_pacientes)
    return jsonify(cadastro_pacientes)

enfermeiras = []

@app.route("/cadastro/enfermeira", methods=['POST'])
def camisetas():
    cadastro_enfermeira = request.json
    for lista in enfermeiras:
        if lista["coren"] == cadastro_enfermeira["coren"]:
            return {"status": "Produto já cadastrado."}
    cadastro_enfermeira = {
        "codigo_barras": str(uuid.uuid4()),
        "coren": cadastro_enfermeira["coren"],
        "senha":cadastro_enfermeira["senha"]
    }
    enfermeiras.append(cadastro_enfermeira)
    return jsonify(cadastro_enfermeira)