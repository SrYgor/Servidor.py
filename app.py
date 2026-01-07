from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite que o jogo Pygame acesse o servidor

ranking = []  # Lista de dicionários {"nome": str, "pontos": int}


@app.route("/ranking")
def get_ranking():
    # Retorna top 50
    top = sorted(ranking, key=lambda x: x["pontos"], reverse=True)[:50]
    return jsonify(top)


@app.route("/adicionar", methods=["POST"])
def adicionar():
    dados = request.json
    nome = dados.get("nome")
    pontos = dados.get("pontos")
    if nome and pontos is not None:
        ranking.append({"nome": nome, "pontos": pontos})
        # Manter top 50
        ranking.sort(key=lambda x: x["pontos"], reverse=True)
        ranking[:] = ranking[:50]
        return jsonify({"sucesso": True})
    return jsonify({"sucesso": False, "erro": "Dados inválidos"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
