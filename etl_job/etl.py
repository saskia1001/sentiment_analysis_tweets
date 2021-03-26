import os
import pymongo
import time
from sqlalchemy import create_engine
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

user = os.getenv('POSTGRES_USER')
password = os.getenv('POSTGRES_PASSWORD')
dbname = os.getenv('POSTGRES_DB')
host = 'postgresdb'
connection_string = f'postgres://{user}:{password}@{host}:5432/{dbname}'

time.sleep(10)  # seconds

# Connect to the MongoDB container
client = pymongo.MongoClient(host='mongodb', port=27017)
db = client.tweet_collector  # Call the db where the tweets are stored
collection = db.tweets

pg = create_engine(connection_string, echo=True)

pg.execute('''
    CREATE TABLE IF NOT EXISTS tweets (
    text VARCHAR(500),
    sentiment NUMERIC
);
''')

# Run a vaderSentiment analysis for each tweet to asign a sentiment
s = SentimentIntensityAnalyzer()

# Write into Postgres
entries = collection.find()
for e in entries:
    text = e['text']
    sentiment = s.polarity_scores(text)
    score = sentiment['compound']
    query = "INSERT INTO tweets VALUES (%s, %s);"
    pg.execute(query, (text, score))

time.sleep(10)
