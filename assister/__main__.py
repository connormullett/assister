
import argparse
import sys

from .api_requester.api_router import ApiRouter

from .todos.todo_router import TodoRouter


parser = argparse.ArgumentParser(description='Productivity without a mouse')
parser.add_argument('command', default=None, action='store', nargs='+')
args = parser.parse_args()

command = args.command[0]
arguments = args.command[1:]

command_mapper = {
        'todo': TodoRouter(arguments),
        'api': ApiRouter(arguments)
        }

if command == 'version':
    sys.stdout.write('0.2.0\n')
    exit(0)

r = command_mapper[command]
r()

