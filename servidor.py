from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista temporária de ranking (vai reiniciar se servidor reiniciar, para algo permanente usar banco de dados)
ranking = []


@app.route('/adicionar', methods=['POST'])
def adicionar():
    data = request.json
    nome = data.get('nome')
    pontos = data.get('pontos')
    if nome and pontos is not None:
        ranking.append({'nome': nome, 'pontos': pontos})
        # Ordena do maior para o menor
        ranking.sort(key=lambda x: x['pontos'], reverse=True)
        # Mantém apenas top 10
        ranking_top10 = ranking[:10]
        return jsonify({'status': 'ok', 'ranking': ranking_top10})
    return jsonify({'status': 'erro', 'mensagem': 'Nome ou pontos faltando'})


@app.route('/ranking', methods=['GET'])
def get_ranking():
    return jsonify(ranking[:10])


if __name__ == '__main__':
    app.run(debug=True)
