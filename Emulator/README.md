## Using Pub/Sub Emulator

**Running the emulator in docker container :**

*Method 1 :*

```sh
docker run --rm -p 8085:8085 google/cloud-sdk:emulators /bin/bash -c "gcloud beta emulators pubsub start --project=some-project-id --host-port='0.0.0.0:8085'"
```

- Replace pubsub with the desired emulator (e.g., `bigtable`, `firestore`).
- Adjust the port mapping (-p 8085:8085) and the `--host-port` flag to match the emulator's default port or your desired port.
- `--project=some-project-id` is a placeholder for the emulator's internal project ID, which does not need to be a real Google Cloud project.

*Method 2 :*

created a docket-compose file .

Run it with this command :

```sh
docker compose -f emulator.docker-compose.yml up
```

**Point your application towards this pubsub :**

As with real GCP Pub/Sub we use service account file & expose *GOOGLE_APPLICATION_CREDENTIALS* env variable to point at that file , but here with Emulator we use following two varibales on the terminal/shell/cmd where we start our code ( publisher or subscriber script ) :

```sh
export PUBSUB_EMULATOR_HOST=localhost:{port}
export PUBSUB_PROJECT_ID={project-id}

# port : the port which you mentioned during container run
    # --host-port arg in Method1
    # --host-port in docker-compose file in Method 2

# project-d : the id which you mentioned during container run
    # --project arg in Method1
    # --project arg in docker-compose file in Method 2
```

## Simple Test

> [Example documentation](https://cloud.google.com/pubsub/docs/emulator) around pub/sub emulator tests .

> Get the Pub/Sub Python samples from  [GitHub](https://github.com/googleapis/python-pubsub)

- basic script are already copied in this 
    - `publisher.py`
    - `subscriber.py`

    you must use these scripts to run the basic tests ( _as explained in next section_ ).
    For testing advanced use cases , you can clone or download the Pub/Sub Python Samples [GitHub](https://github.com/googleapis/python-pubsub)

**Setup the pubsub :**

```sh
# create topic
python3 publisher.py your-project-id create topic-1 # publisher
```

```sh
# create subscription ( pull based )
python3 subscriber.py your-project-id create topic-1 subs-1-pull # pull based subscriber
```

```sh
# create subscription ( push based )
python3 subscriber.py your-project-id create-push topic-1 subs-1-push # pull based subscriber
```

**Simple Test for Pull Based Subscription :**

You can open two terminals , in one you'll publish messages and in other you'll subscribe

```sh
# Terminal 1
python3 publisher.py your-project-id publish topic-1 # will publish some sample messages
```

```sh
# Terminal 2
python3 subscriber.py your-project-id receive subs-1-pull # will start listening on `topic-1`
```


## Developer Samples

Added various sample script folders .
- These depict various operations around Pub/Sub .

It will not contain any complex scenarios . Only simple starter scripts , depicting the core concept .

### Index

| name | description | tags |
| ---- | ----------- | ---- |
| async_pull_sample | this will dmonstrate developing a pull based subscriber | `python` |

