import random
import nltk
import json
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download Portuguese language resources
nltk.download('punkt')
nltk.download('stopwords')

class SentimentAnalyzer:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze_sentiment(self, text):
        sentiment_scores = self.analyzer.polarity_scores(text)
        compound_score = sentiment_scores['compound']

        if compound_score >= 0.1:
            return "happiness"
        elif compound_score <= -0.02:
            return "sadness"
        else:
            return "neutral"

class SentimentChatbot:
    
    def __init__(self):
        super().__init__()
        self.user_score = 0
        self.emotion_mensage = 0
        self.sentiment_analyzer = SentimentAnalyzer()
        self.emotional_support_threshold = 0  # Add emotional_support_threshold attribute
        self.messages = self._load_messages()

    def _load_messages(self):
        with open('mensages.json', 'r') as file:
            messages = json.load(file)
        return messages
    
    def process_input(self, user_input):
        # Check if the user input is a greeting or introduction
        if self._is_greeting(user_input):
            return self.messages["introduction"]

        # Check if the user is requesting emergency phone numbers
        if self._is_emergency_request(user_input):
            self.user_score -= 1
            return self.messages["emergency_numbers"]

        sentiment = self.sentiment_analyzer.analyze_sentiment(user_input)

        # Check if emotional support is needed
        if sentiment == "sadness" and self.user_score < self.emotional_support_threshold:
            # Provide emotional support message
            return self._get_emotional_support_message()

        if sentiment == "happiness":
            self.user_score += 1
            print(self.user_score)
            return "It seems like you're feeling happy! Can I help with anything?"
        elif sentiment == "sadness":
            self.user_score -= 1
            return "I'm sorry to hear that you're feeling sad. Is there something on your mind?"
        elif sentiment == "neutral":
            return "Your sentiment seems neutral. How can I help you today?"
        else:
            return "I'm not sure how you're feeling. Can you tell me more?"

    # functions of the bot!!

    def _is_greeting(self, text):
        # Simple check if the input contains a common greeting
        greetings = self.messages["greetings"]
        return any(greeting in text.lower() for greeting in greetings)
    
    def _is_emergency_request(self, text):
        # Check if the input indicates a request for emergency phone numbers
        emergency_phrases = self.messages["emergency_request"]
        return any(phrase in text.lower() for phrase in emergency_phrases)
    
    def _get_emotional_support_message(self):
        # Return a random emotional support message
        return random.choice(self.messages["emotional_support"])