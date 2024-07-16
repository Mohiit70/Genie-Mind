import os
import tweepy
from transformers import pipeline
from mindsdb import MindsDB
from dotenv import load_dotenv

load_dotenv()

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

# Load MindsDB client
mindsdb = MindsDB()
connection = mindsdb.connect('http://localhost:47334') 
cursor = connection.cursor()

# Load sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")

def fetch_tweets(username, count=10):
    return api.user_timeline(screen_name=username, count=count, tweet_mode='extended')

def simplify_text(text):
    max_len = min(len(text), 50)
    return summarizer(text, max_length=max_len, min_length=10, do_sample=False)[0]['summary_text']

def analyze_sentiment(text):
    query = f"SELECT sentiment FROM mindsdb.sentiment_model WHERE text = '{text}'"
    response = cursor.query(query)
    print(response) 
    sentiment = response.fetch_all()[0]['sentiment']
    return sentiment

def respond_to_tweets(username):
    tweets = fetch_tweets(username)
    for tweet in tweets:
        simplified_text = simplify_text(tweet.full_text)
        sentiment = analyze_sentiment(tweet.full_text)
        response_text = f"Simplified: {simplified_text}\nSentiment: {sentiment}"
        api.update_status(status=response_text, in_reply_to_status_id=tweet.id)