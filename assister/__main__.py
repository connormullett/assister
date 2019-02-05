
import argparse
import sys
from .todo_handler import TodoRouter
# TODO: Add versioning


parser = argparse.ArgumentParser(description='Productivity without a mouse')
parser.add_argument('-t', '--todo', help='create a todo', default=None,
                    action='store', dest='t', nargs='+')
args = parser.parse_args()


def main():

    r = TodoRouter(args.t)
    r()


if __name__ == '__main__':
    main()

