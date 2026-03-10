from flask import Flask

app = Flask(__name__)

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
if __name__ == "__main__":
    app.run(debug=True)
