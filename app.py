'''
Desenvolva uma API que gerencie um cadastro de tarefas
A API tera uma lista de tarefas que devera ter os sequintes campos: ID,
responsavel, tarefa e status
A API devera permitir listar todas as tarefas e tambem incluir novas tarefas
A API devera permitir consultar uma tarefa atraves do ID, alterar o
status de uma tarefa e também excluir uma tarefa
Nenhuma outra alteração devera ser permitira alem do status da tarefa 
'''

from functools import total_ordering
from flask import Flask, request, json, jsonify

app = Flask(__name__)

tarefas = [
    {
        "id" : "0",
        "responsavel" : "Gustavo",
        "tarefa" : "Desenvolver API",
        "status" : "Iniciado"
    },
    {
        "id" : "1",
        "responsavel" : "Andressa",
        "tarefa" : "vendo o codigo",
        "status" : "Iniciado"
    }
]

#listar todas as tarefas e adicionar uma nova
@app.route("/tarefas", methods=["GET", "POST"])
def lista_tarefas():
    if request.method == "GET":
        try:
            response = tarefas
        except Exception:
            response = {
                "status" : "erro",
                "mensagem" : "teste de erro "
            }
        return jsonify(response)
    elif request.method == "POST":
        try:
            dados = json.loads(request.data)
            posicao = len(tarefas)
            dados["id"] = posicao
            tarefas.append(dados)
            response = tarefas[posicao]
        except Exception as err:
            response = {
            "status" : "erro",
            "mensagem" : "teste de erro {} ".format(err)
            }
        return jsonify(response)
        



# retorna, altera e deleta uma tarefa por ID
@app.route("/tarefas/<int:id>", methods=["GET", "PUT", "DELETE"])
def tarefa(id):
    if request.method == "GET":
        try:
            response = tarefas[id]
        except IndexError:
            response = {
                "status" : "erro",
                "mensagem" : "tarefa com a ID {} não encotrada" .format(id)
            }
        except Exception:
            response = {
                "status" : "erro",
                "mensagem" : "teste de erro "
            }
        return jsonify(response)
    elif request.method == "DELETE":
        try:
            tarefas.pop(id)
            response = {
                "status" : "Sucesso",
            "mensagem" : "registro excluido"
            }
        except Exception as err:
            response = {
            "status" : "erro",
            "mensagem" : "teste de erro {} ".format(err)
            }
        return jsonify(response)
    elif request.method == "PUT":
        try:
            dados = json.loads(request.data)
            tarefas[id]["status"] = dados["status"]
            response = {
                "status" : "Sucesso",
            "mensagem" : "registro alterado"
            }
        except Exception as err:
            response = {
            "status" : "erro",
            "mensagem" : "teste de erro {} ".format(err)
            }
        return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)