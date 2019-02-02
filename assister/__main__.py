
import argparse
from .todo_handler import todo_router
# TODO: Add versioning


parser = argparse.ArgumentParser(description='Productivity without a mouse')
parser.add_argument('-t', '--todo', help='create a todo', default=None,
                    action='store', dest='t', nargs='+')
args = parser.parse_args()


def main():

    if len(args.t) > 1:
        todo_router(args.t)

    if args.t:
        todo_router(args.t[0])


if __name__ == '__main__':
    main()

