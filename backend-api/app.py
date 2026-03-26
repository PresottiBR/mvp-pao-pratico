from flask import Flask, request, send_from_directory
from flask_cors import CORS
from flasgger import Swagger
import sqlite3

app = Flask(__name__)
CORS(app)
Swagger(app)


# cria o banco se não existir
def criar_banco():
    conexao = sqlite3.connect("database.db")
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS carregamentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        motorista TEXT,
        veiculo TEXT,
        placa TEXT
    )
    """)

    conexao.commit()
    conexao.close()


# abre o frontend
@app.route("/app")
def abrir_frontend():
    return send_from_directory("../frontend-app", "index.html")


# rota inicial
@app.route("/")
def home():
    return {"mensagem": "API LogControl funcionando"}


# listar todos os carregamentos
@app.route("/carregamentos", methods=["GET"])
def listar_carregamentos():
    """
    Listar todos os carregamentos
    ---
    responses:
      200:
        description: Lista de carregamentos
    """

    conexao = sqlite3.connect("database.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT id, motorista, veiculo, placa FROM carregamentos")
    dados = cursor.fetchall()

    conexao.close()

    lista = []

    for item in dados:
        lista.append({
            "id": item[0],
            "motorista": item[1],
            "veiculo": item[2],
            "placa": item[3]
        })

    return {"carregamentos": lista}


# buscar por id
@app.route("/carregamento/<int:id>", methods=["GET"])
def buscar_carregamento(id):
    """
    Buscar carregamento por id
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    """

    conexao = sqlite3.connect("database.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT id, motorista, veiculo, placa FROM carregamentos WHERE id = ?", (id,))
    dado = cursor.fetchone()

    conexao.close()

    if dado:
        return {
            "id": dado[0],
            "motorista": dado[1],
            "veiculo": dado[2],
            "placa": dado[3]
        }
    else:
        return {"erro": "Não encontrado"}


# criar carregamento
@app.route("/carregamento", methods=["POST"])
def criar_carregamento():
    """
    Criar novo carregamento
    ---
    parameters:
      - in: body
        name: body
        required: true
    """

    dados = request.json

    conexao = sqlite3.connect("database.db")
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO carregamentos (motorista, veiculo, placa) VALUES (?, ?, ?)",
        (dados["motorista"], dados["veiculo"], dados["placa"])
    )

    conexao.commit()
    conexao.close()

    return {"mensagem": "Registrado com sucesso"}


# deletar carregamento
@app.route("/carregamento/<int:id>", methods=["DELETE"])
def deletar_carregamento(id):
    """
    Deletar carregamento
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    """

    conexao = sqlite3.connect("database.db")
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM carregamentos WHERE id = ?", (id,))

    conexao.commit()
    conexao.close()

    return {"mensagem": "Deletado com sucesso"}


if __name__ == "__main__":
    criar_banco()
    app.run(debug=True)