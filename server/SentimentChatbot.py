import re
import nltk
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

        if compound_score >= 0.05:
            return "happiness"
        elif compound_score <= -0.05:
            return "sadness"
        else:
            return "neutral"

class SentimentChatbot:
    
    def __init__(self):
        super().__init__()
        self.user_score = 0
        self.sentiment_analyzer = SentimentAnalyzer()
        self.introduction = (
            "Hi! My name is SentBot. I'm here to help you. "
            "How can I assist you today?"
        )
        self.emergency_numbers_message = (
            "If you need help, here are some emergency phone numbers:\n"
            "Dial 192 - Samu (Mobile Emergency Medical Service)\n"
            "Dial 193 - Fire Department\n"
            "Dial 188 - CVV (Center for Valorization of Life)"
        )

    def process_input(self, user_input):
        # Check if the user input is a greeting or introduction
        if self._is_greeting(user_input):
            return self.introduction

        # Check if the user is requesting emergency phone numbers
        if self._is_emergency_request(user_input):
            return self.emergency_numbers_message

        sentiment = self.sentiment_analyzer.analyze_sentiment(user_input)

        if sentiment == "happiness":
            self.user_score += 1
            return "It seems like you're feeling happy! Can I help with anything?"
        elif sentiment == "sadness":
            self.user_score -= 1
            return "I'm sorry to hear that you're feeling sad. Is there something on your mind?"
        elif sentiment == "neutral":
            return "Your sentiment seems neutral. How can I help you today?"
        else:
            return "I'm not sure how you're feeling. Can you tell me more?"

    def _is_greeting(self, text):
        # Simple check if the input contains a common greeting
        greetings = ["hi", "hello", "hey", "what's up"]
        return any(greeting in text.lower() for greeting in greetings)
    
    def _is_emergency_request(self, text):
        # Check if the input indicates a request for emergency phone numbers
        emergency_phrases = ["would like emergency numbers", "emergency numbers"]
        return any(phrase in text.lower() for phrase in emergency_phrases)
