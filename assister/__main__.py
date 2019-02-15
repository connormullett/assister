
import argparse
import sys

from .api_requester.api_router import ApiRouter

from .todos.todo_router import TodoRouter

with open('config.txt') as cfg:
    VERSION = cfg.read()

parser = argparse.ArgumentParser(description='Productivity without a mouse')
parser.add_argument('command', default=None, action='store', nargs='+')
args = parser.parse_args()


def main():

    command = args.command[0]

    if command == 'version':
        sys.stdout.write(VERSION)
        exit(0)

    if command == 'todo':
        r = TodoRouter(args.command[1:])
    elif command == 'api':
        r = ApiRouter(args.command[1:])
    r()


if __name__ == '__main__':
    main()

