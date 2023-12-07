# your_ml_module.py

import re
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')

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

class SentimentChatbot():
    def __init__(self):
        super().__init__()
        self.sentiment_analyzer = SentimentAnalyzer()

    def process_input(self, user_input):
        sentiment = self.sentiment_analyzer.analyze_sentiment(user_input)

        if sentiment == "happiness":
            return "It seems like you're feeling happy! What's making you feel that way?"
        elif sentiment == "sadness":
            return "I'm sorry to hear that you're feeling sad. Is there something on your mind?"
        elif sentiment == "neutral":
            return "Your sentiment seems neutral. How can I assist you today?"
        else:
            return "I'm not sure how you're feeling. Can you tell me more?"
