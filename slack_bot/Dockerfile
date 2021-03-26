# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Set the working directory to /app -> we define the working directory inside the container to be called /app
WORKDIR /app

# Copy the requirements file into the container at /app
# (a text files with all the libraries you want to install)
COPY requirements.txt /app
# COPY file-on-local-machine directory-in-container

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY slack_bot.py /app

# Run get_tweets.py when the container launches
CMD ["python", "slack_bot.py"]