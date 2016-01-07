import ipaddress
from argparse import ArgumentParser  #  passes variables directly into the app


def create_parser():
    parser = ArgumentParser(
        description='Calculates subnets'
        )
    parser.add_argument(
        'subnet',
        type=str,
        help='Enter an IP subnet'
        )
    return parser.parse_args()


ARGS = create_parser()


def main():
    print(ARGS.subnet)
