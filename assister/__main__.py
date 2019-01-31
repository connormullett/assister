
import sys
import argparse
from .models.todo import Todo
# TODO: Add versioning


parser = argparse.ArgumentParser(description='Productivity without a mouse')
parser.add_argument('-t', '--todo', help='create a todo', default=None,
                    action='store', dest='t')
parser.add_argument('-v', '--verbose', help='perform with detailed input',
                    action='store_true', dest='verbose')
# parser.add_argument('-V', '--version', help='show version number',
#                      action='version', version=_version)
result = parser.parse_args()


def main():
    print('Entered CLI .. ')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))
    if result.verbose:
        print('Verbosity enabled')
    if result.t:
        print(result.t)


if __name__ == '__main__':
    main()

