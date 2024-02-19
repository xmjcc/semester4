import argparse

DEFAULT_PORT = 12345
DEFAULT_PROTOCOL = 'tcp'

parser = argparse.ArgumentParser()
parser.add_argument(
    dest='role',
    help='either server or client'
)

args = parser.parse_args()

print(args.role)