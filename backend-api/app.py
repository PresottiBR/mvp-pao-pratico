from flask import Flask, request, send_from_directory
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def criar_banco():
    conexao = sqlite3.connect("database.db")
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS carregamentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        motorista TEXT,
        veiculo TEXT,
        placa TEXT,
        produto TEXT,
        destino TEXT,
        km_planejado INTEGER,
        km_rodado INTEGER,
        data TEXT
    )
    """)

    conexao.commit()
    conexao.close()

@app.route("/app")
def abrir_frontend():
    return send_from_directory("../frontend-app", "index.html")    

@app.route("/")
def home():
    return {"mensagem": "API do sistema LogControl funcionando"}

@app.route("/carregamentos")
def listar_carregamentos():

    conexao = sqlite3.connect("database.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT motorista, veiculo, placa FROM carregamentos")

    registros = cursor.fetchall()

    conexao.close()

    lista = []

    for r in registros:
        lista.append({
            "motorista": r[0],
            "veiculo": r[1],
            "placa": r[2]
        })

    return {"carregamentos": lista}
        
@app.route("/carregamento", methods=["POST"])
def criar_carregamento():

    dados = request.json

    conexao = sqlite3.connect("database.db")
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO carregamentos
        (motorista, veiculo, placa)
        VALUES (?, ?, ?)
    """, (
        dados["motorista"],
        dados["veiculo"],
        dados["placa"]
    ))

    conexao.commit()
    conexao.close()

    return {"mensagem": "Carregamento registrado com sucesso"}

if __name__ == "__main__":
    criar_banco()
    app.run(debug=True)
