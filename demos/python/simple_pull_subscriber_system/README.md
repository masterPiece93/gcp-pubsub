# Simple Pull Subscriber System

## Explaination : Watch
> add video log

## How to Run

> you can also refer the video above for the `how to run`

**Step 1**

run pubsub
    - either you'll be having a GCP pubsub running
    - or, [run the emulator](../../../Emulator) 
        
once you have pubsub running, set the environment variables in `__init__.py` file as per the instructions mentioned there .

**Step 2**

Run Subscriber code : open a terminal/shell/cmd & run :

```sh
python3 -m simple_pull_subscriber_system --run-subscriber --on-emulator
```

Run Publisher code : open a terminal/shell/cmd & run :

```sh
python3 -m simple_pull_subscriber_system --run-publisher --on-emulator
```

explaination :

- in `main.py` we have written argument parsing logic , hence `--run-subscriber`, `--run-publisher` & `--on-emulator` are handled in that file .
    - `--run-subscriber` & `--run-publisher` are made mutually exclusive argument , you can specify nly one of them .
    - if `--run-subscriber` is specified , we call `subscriber_code.py` file , it starts a non-blocking & always listening pubsub subscriber .
    - if `--run-publisher` is specified , we call `publisher_code.py` file , it sends some messages on pubsub .
    - if `--on-emulator` is specified , we call **setup()** method .

- some basic configurations like topic_id, subscription_name etc are governed from `__init__.py` file .
    - In case of emulator , whatever values you enter there , **setup()** creates them for you .
    - In case of real pubsub , you have to get these things created , procure a service-account.json file and set them there .