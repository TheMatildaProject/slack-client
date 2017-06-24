class Slack(self):

        sc.api_call(
                    'chat.postMessage',
                    channel=channel,
                    text="HAHAHAH!",
                    as_user='true:'
                )