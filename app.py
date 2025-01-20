from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)  # Permite requisições externas de outros domínios

# Substitua pela sua API Key da OpenAI
openai.api_key = "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"

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Verifica se a mensagem foi enviada no corpo da requisição
        user_message = request.json.get('message')
        if not user_message:
            return jsonify({"error": "Mensagem não fornecida"}), 400

        # Chamada à API moderna da OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Substitua pelo modelo correto, se necessário
            messages=[
                {"role": "system", "content": "Você é um assistente útil e amigável."},
                {"role": "user", "content": user_message}
            ]
        )
        # Retorna a resposta do assistente
        return jsonify({"response": response.choices[0].message['content']})

    except openai.error.AuthenticationError:
        return jsonify({"error": "API Key inválida ou ausente"}), 401
    except openai.error.RateLimitError:
        return jsonify({"error": "Limite de requisições da API foi excedido"}), 429
    except Exception as e:
        # Exibe o erro no log do Render
        print(f"Erro no servidor: {str(e)}")
        return jsonify({"error": "Erro interno no servidor"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

