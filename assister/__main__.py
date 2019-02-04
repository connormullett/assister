
import argparse
import sys
from .todo_handler import todo_router
# TODO: Add versioning


parser = argparse.ArgumentParser(description='Productivity without a mouse')
parser.add_argument('-t', '--todo', help='create a todo', default=None,
                    action='store', dest='t', nargs='+')
args = parser.parse_args()


def main():

    if args.t is None:
        sys.stdout.write('No Arguments given\n' +
                         'Use assister -h for commands\n')
        sys.exit(0)

    if len(args.t) > 1:
        todo_router(args.t)

    if args.t:
        todo_router(args.t[0])


if __name__ == '__main__':
    main()

