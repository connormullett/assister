
from .models import todo


def handler(t):

    if t.lower() == 'create':
        print('gonna create a todo')

    elif t.lower() == 'del':
        pass

    elif t.lower() == 'update':
        pass

    elif t.lower() == 'mc':
        pass

    elif t.lower() == 'mi':
        pass

    elif t.lower() == 'cdue':
        pass

    elif t.lower() == 'view':
        pass

    elif t.lower() == 'get':
        pass

    else:
        print('unknown argument')


