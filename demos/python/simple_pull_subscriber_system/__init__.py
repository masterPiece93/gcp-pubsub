"""
Setup
"""
import os

# Developer can Set the following values from .env file 
# # - following values are associated with pubsub
# # - if you have stared an emulator , and have not created following values , don't worry , 
# #     whatever value you will enter here , it will be automaticallu created when you run this example .
# #     
__PROJECT_ID__ = "test"
__TOPIC_NAME__ = "test-topic"
__SUBSCRIPTION_NAME__ = "test-topic-subs-pull"
__EMULATOR__PORT__ = 8085                           # if application is running on Emulator
__GCP_SERVICE_ACCOUNT_FILE_PATH__ = "./gcp.json"    # if application uses Real Pubsub on GCP , e.g:"absolute/path/to/service_account_file.json"

# Utility :
def create_topic(project_id: str, topic_id: str) -> None:
    """Create a new Pub/Sub topic."""
    # [START pubsub_quickstart_create_topic]
    # [START pubsub_create_topic]
    from google.cloud import pubsub_v1

    # TODO(developer)
    # project_id = "your-project-id"
    # topic_id = "your-topic-id"

    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_id)

    topic = publisher.create_topic(request={"name": topic_path})

    print(f"Created topic: {topic.name}")
    # [END pubsub_quickstart_create_topic]
    # [END pubsub_create_topic]

# Utility :
def create_subscription(project_id: str, topic_id: str, subscription_id: str) -> None:
    """Create a new pull subscription on the given topic."""
    # [START pubsub_create_pull_subscription]
    from google.cloud import pubsub_v1

    # TODO(developer)
    # project_id = "your-project-id"
    # topic_id = "your-topic-id"
    # subscription_id = "your-subscription-id"

    publisher = pubsub_v1.PublisherClient()
    subscriber = pubsub_v1.SubscriberClient()
    topic_path = publisher.topic_path(project_id, topic_id)
    subscription_path = subscriber.subscription_path(project_id, subscription_id)

    # Wrap the subscriber in a 'with' block to automatically call close() to
    # close the underlying gRPC channel when done.
    with subscriber:
        subscription = subscriber.create_subscription(
            request={"name": subscription_path, "topic": topic_path}
        )

    print(f"Subscription created: {subscription}")
    # [END pubsub_create_pull_subscription]

def setup(is_emulator: bool):
    """setup the environment and pubsub
    """

    os.environ.setdefault("PUBSUB_TOPIC_NAME", __TOPIC_NAME__)
    os.environ.setdefault("PUBSUB_SUBSCRIPTION_NAME", __SUBSCRIPTION_NAME__)
        
    if is_emulator == True:
        from google.api_core.exceptions import AlreadyExists

        # Emulator
        os.environ["PUBSUB_EMULATOR_HOST"] = f"localhost:{__EMULATOR__PORT__}" # <- for Emulator Pub/Sub
        os.environ["PUBSUB_PROJECT_ID"] = __PROJECT_ID__ # <- for Emulator Pub/Sub

        print(f"Current Project : {__PROJECT_ID__}")
        # create topic
        try:
            create_topic(__PROJECT_ID__, __TOPIC_NAME__)
        except AlreadyExists:
            print(f"topic : {__TOPIC_NAME__} already created for project id - `{__PROJECT_ID__}`")
        
        # create pull type subscription
        try:
            create_subscription(__PROJECT_ID__, __TOPIC_NAME__, __SUBSCRIPTION_NAME__)
        except AlreadyExists:
           print(f"subscription : {__SUBSCRIPTION_NAME__} already created for project id - `{__PROJECT_ID__}`")
    else:

        # Real
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = __GCP_SERVICE_ACCOUNT_FILE_PATH__ # <- for Real Pub/Sub

# utilities
def get_datetime_ist():
    from datetime import datetime
    from zoneinfo import ZoneInfo

    utc_now = datetime.now(ZoneInfo("UTC"))
    ist_zone = ZoneInfo("Asia/Kolkata")
    ist_time = utc_now.astimezone(ist_zone)
    return ist_time