import os
import time
from slackclient import SlackClient
from app.services.corpus_callosum import CorpusCallosum

token = os.environ['SLACK_TOKEN']
sc = SlackClient(token)

if sc.rtm_connect():
    while True:
        events = sc.rtm_read()
        for event in events:
            # Narowing down event types
            # Make sure there's a channel to respond back, there is text, the event type is of message
            # And most importantly to avoid loop, verify if wasn't a bot who sent the message, in which case
            # Matilda would just be forever talking to herself
            if ('channel' in event and 'bot_id' not in event and 'text' in event and event.get('type') == 'message'):
                cc = CorpusCallosum(event);
                
else:
    print ("Connection Failed, invalid token?")

if __name__ == "__main__":
    app.run(debug=True)