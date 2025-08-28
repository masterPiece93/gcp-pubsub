import argparse
from . import setup

parser = argparse.ArgumentParser(
    prog="Simple Pull Based Pub/Sub System",
    description="",
    epilog=""
)

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--run-publisher', action="store_true", help="Executes Publisher Code")
group.add_argument('--run-subscriber', action="store_true", help="Executes Subscriber Code")
parser.add_argument('--on-emulator', action="store_true", help="Specifies If needs to be run on emulator")
args = parser.parse_args()

setup(is_emulator=args.on_emulator)

if args.run_publisher == True:
    from .publisher_code import run
    # from demos.python.simple_pull_subscriber_system.publisher_code import run
    run()

if args.run_subscriber == True:
    from .subscriber_code import *
    

