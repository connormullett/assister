
import argparse
import sys

from .api_requester.api_router import ApiRouter

from .todos.todo_router import TodoRouter
# TODO: Add versioning


parser = argparse.ArgumentParser(description='Productivity without a mouse')
parser.add_argument('command', default=None, action='store', nargs='+')
# parser.add_argument('-a', '--api', help='perform api requests', default=None, action='store', dest='a', nargs='+')
args = parser.parse_args()


def main():

    command = args.command[0]
    if command == 'todo':
        r = TodoRouter(args.command[1:])
    elif command == 'api':
        r = ApiRouter(args.command[1:])
    r()


if __name__ == '__main__':
    main()

