from flask import Flask, jsonify, request

app = Flask(__name__)

# Rota inicial
@app.route("/")
def home():
    return jsonify({"mensagem": "API Flask funcionando!"})

# Rota GET (listar usuarios)
@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    itens = [
        {"id": 1, "nome": "Maria"},
        {"id": 2, "nome": "Thiago"},
        {"id": 3, "nome": "Marcos"},
        {"id": 4, "nome": "Leticia"},
        {"id": 5, "nome": "Lucas"},
        {"id": 6, "nome": "Mariana"},
        {"id": 7, "nome": "Eduardp"},
        {"id": 8, "nome": "Carla"},
    ]
    return jsonify(itens)

# Rota POST (adicionar item)
@app.route("/usuarios", methods=["POST"])
def adicionar_usuario():
    novo_item = request.get_json()
    return jsonify({"mensagem": "Item adicionado com sucesso!", "item": novo_item}), 201

# Rota GET com parâmetro
@app.route("/usuarios/<int:item_id>", methods=["GET"])
def buscar_item(item_id):
    return jsonify({"id": item_id, "nome": f"Item {item_id}"})

if __name__ == "__main__":
    app.run(debug=True)
