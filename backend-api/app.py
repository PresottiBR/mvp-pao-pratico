from flask import Flask, request
import sqlite3

app = Flask(__name__)
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

@app.route("/")
def home():
    return {"mensagem": "API do sistema Pão Prático funcionando"}
@app.route("/carregamentos")
def listar_carregamentos():
    return {
        "carregamentos": [
            {
                "motorista": "João",
                "carro": "Caminhão",
                "produto": "Pão Francês",
                "destino": "Padaria Central",
                "valor_abastecimento": 150.00,
                "km_saída": 45,
                "km_chegada": 47
            }
        ]
    }
@app.route("/carregamento", methods=["POST"])
def criar_carregamento():

    dados = request.json

    conexao = sqlite3.connect("database.db")
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO carregamentos
        (motorista, veiculo, placa, produto, destino, km_planejado, km_rodado, data)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        dados["motorista"],
        dados["veiculo"],
        dados["placa"],
        dados["produto"],
        dados["destino"],
        dados["km_planejado"],
        dados["km_rodado"],
        dados["data"]
    ))

    conexao.commit()
    conexao.close()

    return {"mensagem": "Carregamento registrado com sucesso"}

if __name__ == "__main__":
    criar_banco()
    app.run(debug=True)
