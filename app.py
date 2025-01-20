from flask import Flask, request, jsonify
from flask_cors import CORS  # Permite requisições externas
import openai

app = Flask(__name__)
CORS(app)  # Habilita CORS para permitir requisições de outros domínios

# Substitua pela sua API Key da OpenAI
openai.api_key = "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"

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')  # Obtém a mensagem do usuário
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Substitua pelo modelo correto, se necessário
        messages=[
            {"role": "system", "content": "Você é um assistente útil e amigável."},
            {"role": "user", "content": user_message}
        ]
    )
    return jsonify({"response": response.choices[0].message['content']})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
