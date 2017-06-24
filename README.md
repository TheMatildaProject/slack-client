# Slack Client
Allows direct connection to Corpus Callosum through Slack

## Installation

Make sure `.env` is filled based on `.env.example`

### Build
docker build . -t slack-client

### Run
docker run -t --env-file .env --name slack-client  -v $(pwd):/app slack-client python /app/slack-listener.py

docker run -t --env-file .env --name slack-client  -v $(pwd):/app slack-client python /app/channel-listener.py
