import os
import tweepy
from transformers import pipeline

# Initialize Twitter API
auth = tweepy.OAuthHandler(
    os.getenv('TWITTER_CONSUMER_KEY'),
    os.getenv('TWITTER_CONSUMER_SECRET')
)
auth.set_access_token(
    os.getenv('TWITTER_ACCESS_TOKEN'),
    os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
)
api = tweepy.API(auth)

# Load text summarization pipeline
summarizer = pipeline("summarization")

# Load sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")

def fetch_tweets(username, count=10):
    return api.user_timeline(screen_name=username, count=count, tweet_mode='extended')

def simplify_text(text):
    input_length = len(text.split())
    max_length = min(50, input_length)  # Adjust max_length based on input length
    return summarizer(text, max_length=max_length, min_length=max_length//2, do_sample=False)[0]['summary_text']


def analyze_sentiment(text):
    response = sentiment_analyzer(text)[0]
    return response['label']


def respond_to_tweets(username):
    tweets = fetch_tweets(username)
    for tweet in tweets:
        simplified_text = simplify_text(tweet.full_text)
        sentiment = analyze_sentiment(tweet.full_text)
        response_text = f"Simplified: {simplified_text}\nSentiment: {sentiment}"
        api.update_status(status=response_text, in_reply_to_status_id=tweet.id)
