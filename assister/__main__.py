
import argparse
import sys
import pkg_resources

from .api_requester.api_router import ApiRouter
from .todos.todo_router import TodoRouter

VERSION = pkg_resources.require('assister')[0].version

parser = argparse.ArgumentParser(description='Productivity without a mouse')
parser.add_argument('command', default=None, action='store', nargs='+')
args = parser.parse_args()

def main():
    command = args.command[0]
    arguments = args.command[1:]

    command_mapper = {
            'todo': TodoRouter,
            'api': ApiRouter
            }

    if command == 'version':
        sys.stdout.write(f'{VERSION}\n')
        exit(0)

    r = command_mapper[command]
    i = r(arguments)
    i()

if __name__ == '__main__':
    main()

