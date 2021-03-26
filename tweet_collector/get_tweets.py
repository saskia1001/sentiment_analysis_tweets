import os
from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener
import json
import logging
import pymongo

# Get keys for the Twitter API from the environment.
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

# Connect to the MongoDB container.
client = pymongo.MongoClient(host='mongodb', port=27017)

# Create a new database to store the tweets.
db = client.tweet_collector

# Define a collection
collection = db.tweets


def authenticate():
    """Function for handling Twitter Authentication. Please note
       that this script assumes you have a file called config.py
       which stores the 4 required authentication tokens:

       1. API_KEY
       2. API_SECRET
       3. ACCESS_TOKEN
       4. ACCESS_TOKEN_SECRET

    See course material for instructions on getting your own Twitter credentials.
    """
    auth = OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    return auth


class TwitterListener(StreamListener):

    def on_data(self, data):
        """Whatever we put in this method defines what is done with
        every single tweet as it is intercepted in real-time"""

        t = json.loads(data)  # t is just a regular python dictionary.

        tweet = {
            'text': t['text'],
            'username': t['user']['screen_name'],
            'followers_count': t['user']['followers_count']
        }

        # Insert the Tweets in a collection, namely tweets.
        collection.insert(tweet)

        logging.critical(f'\n\n\nTWEET INCOMING: {tweet["text"]}\n\n\n')

    def on_error(self, status):

        if status == 420:
            print(status)
            return False


if __name__ == '__main__':

    auth = authenticate()
    listener = TwitterListener()
    stream = Stream(auth, listener)
    stream.filter(track=['machine learning'], languages=['en'])
