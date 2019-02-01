
import argparse
from .todo_handler import todo_router
# TODO: Add versioning


parser = argparse.ArgumentParser(description='Productivity without a mouse')
parser.add_argument('-t', '--todo', help='create a todo', default=None,
                    action='store', dest='t')
args = parser.parse_args()


def main():
    print('Entered CLI .. ')

    if args.t:
        todo_router(args.t)


if __name__ == '__main__':
    main()

