import ast
import json
import os
import redis
from slackclient import SlackClient

r = redis.StrictRedis(host=os.environ['REDIS'])
pubsub = r.pubsub()
pubsub.subscribe('slack')

print ('Listening...')

# Converts ' into " :(
def nastyWorkaround(string):
    string = string.replace("{'", '{"')
    string = string.replace("'}", '"}')

    string = string.replace("':", '":')
    string = string.replace(": '", ': "')
    string = string.replace(", '", ', "')
    string = string.replace("',", '",')

    return string
    
while True:
    for item in pubsub.listen():
        
        if (item['data'] != 1):
            message = json.dumps(item['data'].decode('utf-8'))
            message = ast.literal_eval(message)
            message = nastyWorkaround(message)

            message = json.loads(message)

            sc = SlackClient(message['token'])

            sc.api_call(
                'chat.postMessage',
                channel=message['channel'],
                text=message['text'],
                as_user='true:' 
            )
            

