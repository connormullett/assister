
import argparse
from .todo_handler import handler
# TODO: Add versioning


parser = argparse.ArgumentParser(description='Productivity without a mouse')
parser.add_argument('-t', '--todo', help='create a todo', default=None,
                    action='store', dest='t')
args = parser.parse_args()


def main():
    print('Entered CLI .. ')

    if args.t:
        handler(args.t)


if __name__ == '__main__':
    main()

