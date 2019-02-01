
import sys
import argparse
from .models.todo import Todo
# TODO: Add versioning


parser = argparse.ArgumentParser(description='Productivity without a mouse')
parser.add_argument('-t', '--todo', help='create a todo', default=None,
                    action='store', dest='t')
# parser.add_argument('-v', '--verbose', help='perform with detailed input',
#                     action='store_true', dest='verbose')
# parser.add_argument('-V', '--version', help='show version number',
#                      action='version', version=_version)
args = parser.parse_args()


def main():
    print('Entered CLI .. ')

    if args.t:
        pass


if __name__ == '__main__':
    main()

