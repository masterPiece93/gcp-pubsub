"""
This script is depicting the application that
    needs to send the messages .
"""

import os
import time
import json
from google.cloud import pubsub_v1
from datetime import datetime
from zoneinfo import ZoneInfo


# Replace with your project ID and topic name
project_id = os.environ["PUBSUB_PROJECT_ID"]
topic_name = os.environ["PUBSUB_TOPIC_NAME"]

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_name)

def publish_json(data):
    """Publishes a message to a Pub/Sub topic."""
    data = json.dumps(data, ensure_ascii=False).encode('utf8')
    future = publisher.publish(topic_path, data)
    print(f"{datetime.now(ZoneInfo("Asia/Kolkata")).strftime("[%I:%M:%S-%p]")} :: Published message ID: {future.result()}")

def run():
    publish_json({"duration":30})
    publish_json({"duration":60})
    time.sleep(10)
    publish_json({"duration":30})

if __name__ == "__main__":
    publish_json({"duration":30})