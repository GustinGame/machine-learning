from flask import Flask, request, jsonify
from flask_cors import CORS  # Import the CORS module
from SentimentChatbot import SentimentChatbot

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
sentiment_chatbot = SentimentChatbot()

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        message = data['message']

        # Call your SentimentChatbot to process the input
        response = sentiment_chatbot.process_input(message)

        return jsonify({'response': response})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
