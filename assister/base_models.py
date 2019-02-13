
import sys

class WriteOut:

    def __call__(self, msg, code=None):
        sys.stdout.write(msg + '\n')
        if code is 0 or code:
            sys.exit(code)


class ReadOut:

    def __call__(self, msg):
        i = input(msg + '\n>>> ')
        return i

