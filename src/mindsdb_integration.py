import requests
from config.config import MINDSDB_ENDPOINT

def get_sentiment_prediction(review_text):
    response = requests.post(MINDSDB_ENDPOINT, json={
        'model': 'sentiment_predictor',
        'data': {'review_text': review_text}
    })
    return response.json()['sentiment']
