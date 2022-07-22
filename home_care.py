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
        "codigo": str(uuid.uuid4()),
        "coren": cadastro_enfermeira["coren"],
        "senha":cadastro_enfermeira["senha"]
    }
    enfermeiras.append(cadastro_enfermeira)
    return jsonify(cadastro_enfermeira)

@app.route("/login/pacientes", methods=['POST'])
def logar():
    login_pacientes = request.json
    for login_pacientes in Paciente:
        if login_pacientes["cpf"] == login_pacientes["cpf"] and login_pacientes["senha"] == login_pacientes["senha"]:
            return{"Paciente.":"Logado."}
        else:
            return{"Status":"Cpf ou Senha Incorretos."}


@app.route("/login/enfermeira", methods=['POST'])
def logar():
    login = request.json
    for login in enfermeiras:
        if login["coren"] == login["coren"] and login["senha"] == login["senha"]:
            return{"enfermeira(o)":"Logado."}
        else:
            return{"Status":"coren ou Senha Incorretos."}

@app.route("/banco_de_dados/pacientes")
def pacientes_dados():
    return jsonify(Paciente)

@app.route("/banco_de_dados/enfermeiras(o)")
def enfermeiros_dados():
    return jsonify(enfermeiras)

@app.route("/banco_de_dados")
def banco_de_dados():
    return jsonify(Paciente,enfermeiras)

@app.route("/excluir/pacientes", methods=['POST'])
def excluir_pacientes():
    pacientes_excluir = request.json
    print(Paciente)
    for listas in Paciente:
        if listas["id"] == pacientes_excluir["id"]:
            Paciente.remove(listas)
            return pacientes_excluir


@app.route("/excluir/enfemeiras", methods=['POST'])
def excluir_enfemeiras():
    enfermeiras_excluir = request.json
    print(enfermeiras)
    for listagem in enfermeiras:
        if listagem["codigo"] == enfermeiras_excluir["codigo"]:
            enfermeiras.remove(listagem)
            return enfermeiras_excluir