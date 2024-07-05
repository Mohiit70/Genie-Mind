import mysql.connector
from src.mindsdb_integration import get_sentiment_prediction
from src.twitter_bot import authenticate_twitter, fetch_tweets, reply_to_tweet
from config.config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

def main():
    # Connect to MySQL database
    db = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )
    cursor = db.cursor()

    # Fetch reviews from the database
    cursor.execute("SELECT review_text FROM reviews")
    reviews = cursor.fetchall()

    for review in reviews:
        review_text = review[0]
        predicted_sentiment = get_sentiment_prediction(review_text)
        print(f"Review: {review_text}")
        print(f"Predicted Sentiment: {predicted_sentiment}")
        print("")

    cursor.close()
    db.close()

    # Authenticate with Twitter
    api = authenticate_twitter()

    # Fetch recent tweets containing a specific hashtag
    search_query = '#YourHashtag -filter:retweets'
    tweets = fetch_tweets(api, search_query)

    # Reply to tweets based on sentiment analysis
    for tweet in tweets:
        tweet_text = tweet.text
        predicted_sentiment = get_sentiment_prediction(tweet_text)
        print(f"Tweet: {tweet_text}")
        print(f"Predicted Sentiment: {predicted_sentiment}")

        if predicted_sentiment == 'positive':
            reply_text = "Thank you for the positive feedback! 😊"
        elif predicted_sentiment == 'negative':
            reply_text = "We're sorry to hear that. Can you tell us more about what went wrong?"
        else:
            reply_text = "Thanks for sharing your thoughts!"

        reply_to_tweet(api, tweet, reply_text)
        print(f"Replied with: {reply_text}")
        print("")

if __name__ == '__main__':
    main()
