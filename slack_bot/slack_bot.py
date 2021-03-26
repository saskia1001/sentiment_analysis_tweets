import requests
from sqlalchemy import create_engine
import os

# Postgres access variables
user = os.getenv('POSTGRES_USER')
password = os.getenv('POSTGRES_PASSWORD')
dbname = os.getenv('POSTGRES_DB')
host = 'postgresdb'
connection_string = f'postgres://{user}:{password}@{host}:5432/{dbname}'
# Slack access variables
webhook_url = os.getenv('WEBHOOK')

# Create a connection to Postgres
pg = create_engine(connection_string, echo=True)

tweet_data = pg.execute('''
    SELECT text FROM tweets WHERE sentiment > 0 LIMIT 5;
''')

for tweet_text in tweet_data:
    data = {'text': tweet_text[0]}
    requests.post(url=webhook_url, json=data)
