import os
import requests

class CorpusCallosum(object):
    def __init__(self, slack_event):
        channel = slack_event['channel']
        text = slack_event['text']

        payload = {
            "action": "command",
            "parameters": {
                "text": text,
                "channel": channel,
                "token": os.environ['SLACK_TOKEN'],
            },
            "origin": "slack"
        }

        rq = requests.post(os.environ["CORPUS_CALLOSUM"], json=payload);