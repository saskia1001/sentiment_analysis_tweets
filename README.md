# Sentiment Anaylsis of Tweets with a Dockerized Data Pipeline
![data_pipeline](data_pipeline.jpg)\
Data Pipeline
## Project Description
Dockerized Data Pipeline that analyzes the sentiment of tweets and posts to Slack.

## Requirements
* Docker: Install [Docker](https://docs.docker.com/). To get you started, this [Turorial](https://www.youtube.com/watch?v=YFl2mCHdv24&t=3s&ab_channel=JakeWright) by Jake Wright might help you.
* Slack: To set up the Slack bot, you need to create a [new Slack app](https://api.slack.com/apps) and note the *Webhooks* (to be used in `slack_bot/slack_bot.py.py`).
* Twitter: Create a [developer account](apps.twitter.com) and note your *API Key*, *API Secret*, *Access Token*, *Access Token Secret* (to be used in `tweet_collector/get_tweets.py`)

The necessary Python packages are documented in the particular `requirements.txt` files in each subfolder. With running the script the necessary packages will be installed. All keys are stored as environment variables in the presented code due to privacy. I highly recommend this approach when sharing your code with others.

## Usage
To run the data pipeline with all Docker containers and the corresponding databases and applications, enter the following bash command `docker-compose up -d` to build, create and start the entire pipeline in the background.

## Final notes
Of course, you could get the same done with less machinery, but this project is built as a Data Engineering project and to get into the basics of Docker. There is also room for improvement in the sentiment analysis. The project was part of my [SPICED Data Science Bootcamp](https://www.spiced-academy.com/en/program/data-science).