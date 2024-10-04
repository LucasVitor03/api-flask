from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return jsonify({'mensagem': 'Bem-vindo à API Flask!'})

@app.route('/enviar-dados', methods=['POST'])
def receber_dados():  # put application's code here
    dados = request.get_json()
    return jsonify({'mensagem': 'Dados recebidos com sucesso', 'dados': dados})

#Endpoint com parâmetros na URL
@app.route('/usuario/<nome>', methods=['GET'])
def obter_usuario(nome):
    return jsonify({'mensagem': f'Olá, {nome}!'})

if __name__ == '__main__':
    app.run(debug=True)
