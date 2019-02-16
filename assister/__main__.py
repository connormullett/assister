
import argparse
import sys
import pkg_resources
import os

from .api_requester.api_router import ApiRouter
from .todos.todo_router import TodoRouter
from .dir_builder.dir_router import DirectoryRouter

def main():

    VERSION = pkg_resources.require('assister')[0].version

    parser = argparse.ArgumentParser(description='Productivity without a mouse')
    parser.add_argument('command', default=None, action='store', nargs='+')
    parser.add_argument('-p', '--progress', dest='p', default=False, action='store_true')
    parser.add_argument('-g', '--greet', dest='g', default=False, action='store_true')
    args = parser.parse_args()

    command = args.command[0]
    arguments = args.command[1:]

    command_mapper = {
            'todo': TodoRouter,
            'api': ApiRouter,
            'dir': DirectoryRouter,
            }

    if command == 'version':
        sys.stdout.write(f'ASSISTER VERSION | {VERSION}\n')
        exit(0)

    if args.g:
        user = os.getlogin()
        print(f'Hello, {user}')

    r = command_mapper[command]
    i = r(arguments)
    i()

