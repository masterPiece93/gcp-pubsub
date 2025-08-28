"""
This script is depicting the application that
    needs to listen to the messages .
"""
import os, sys
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)

import json
from concurrent.futures import TimeoutError
from google.cloud import pubsub_v1
from processing import ComplexProcess
from datetime import datetime
from zoneinfo import ZoneInfo

# NOTE : To be set by developer , preferably taken from environment variable
project_id = os.environ["PUBSUB_PROJECT_ID"]
subscription_id = os.environ["PUBSUB_SUBSCRIPTION_NAME"]

# Instantiating the subscriber client
subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_id, subscription_id)

# Callback
def callback(message: pubsub_v1.subscriber.message.Message) -> None:
    """
    This is the Callback function .
    This will be called every time ( with a new message object ) a message is received by the subscriber .
    """
    message_id = message.message_id
    message_data = message.data.decode('utf-8')
    print(f"{datetime.now(ZoneInfo("Asia/Kolkata")).strftime("[%I:%M:%S-%p]")} :: message : ID:{message_id} DATA:{message_data}")
    try: # message.data is a raw text , to read it as a python dict we do the following :
        json_payload = json.loads(message.data.decode('utf-8'))
    except Exception as e:
        ...
        # log > with message-id
        # publish to some other topic add<prev.-message-id>
        ## in some scenrios , you need to intimate next application of the status .
        ## So here you can do that .
        print(e)
        message.nack() # <- This will put the message back in queue for retry . :REFER 
    else:
        # message.ack() # NOTE : never acknowledge a message before processing .
        ComplexProcess('linear').run(message_id, json_payload)
        print(f"{datetime.now(ZoneInfo("Asia/Kolkata")).strftime("[%I:%M:%S-%p]")} :: Process with duration : {json_payload["duration"]} [ID:{message_id}] completed now.")
        message.ack() # EXPERIMENT 1

streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
print(f"Listening for messages on {subscription_path}..\n")

# Wrap subscriber in a 'with' block to automatically call close() when done.
with subscriber:
    try:
        streaming_pull_future.result(timeout=None)
    except TimeoutError:
        streaming_pull_future.cancel()  # Trigger the shutdown.
        streaming_pull_future.result()  # Block until the shutdown is complete.


# EXPERIMENT 1
## you can try commenting message.ack()
## you will find that your processing runs as usual
## but now do either of the two things :
##  - stop and rerun the subscriber
##  - start another fresh new subscriber
## you will notice that all the messages that you processed , will
## now reappear to your subscriber !!
## Why ? - because you didn't ackowledge the message 