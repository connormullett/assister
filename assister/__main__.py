
import sys


def main():
    print('Entered CLI .. ')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))


if __name__ == '__main__':
    main()

