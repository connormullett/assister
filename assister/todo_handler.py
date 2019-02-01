
import sys
import os
import csv


def get_rows():
    f = open(os.path.dirname(__file__) + '/todo.csv')
    reader = csv.reader(f, delimiter=',')
    rows = []
    for row in reader:
        rows.append(row)
    return rows


def todo_create():
    # helper function for string columns
    def get_id():
        rows = get_rows()
        del rows[0]
        for i, x in enumerate(rows):
            if i + 1 != x:
                return i + 1

    while True:
        title = input('Enter title( max 20 )\n>>> ')
        content = input('Enter Content ( max 50 )\n>>> ')
        due = input('Enter due date ( yy/mm/dd )\n>>> ')
        todo_id = get_id()


def todo_router(t):

    if t.lower() == 'create':
        todo_create()

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
        sys.stdout.write('viewing todos\n')

    elif t.lower() == 'get':
        pass

    else:
        print('unknown argument')


