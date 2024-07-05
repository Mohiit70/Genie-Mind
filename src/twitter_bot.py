import tweepy
from config.config import (TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET,
                           TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

def authenticate_twitter():
    auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    return api

def fetch_tweets(api, query, count=10):
    tweets = tweepy.Cursor(api.search_tweets, q=query, lang="en").items(count)
    return tweets

def reply_to_tweet(api, tweet, reply_text):
    api.update_status(status=reply_text, in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
