
import sys
import os
import csv

TODO_FILE = os.path.dirname(__file__) + '/todo.csv'


def get_rows():
    f = open(TODO_FILE)
    reader = csv.reader(f, delimiter=',')
    rows = []
    for row in reader:
        rows.append(row)
    return rows


def get_id():
    # this is garbage im sorry
    rows = get_rows()
    _ = []
    for row in rows:
        _.append(row[0])
    del _[0]
    todos = []
    for i in _:
        a = int(i)
        todos.append(a)

    todos = todos.sort()
    return next(a for a, b in enumerate(todos, 1) if a != b)


def todo_create():

    # while True:
    title = input('Enter title( max 20 )\n>>> ')
    content = input('Enter Content ( max 50 )\n>>> ')
    due = input('Enter due date ( yy/mm/dd )\n>>> ')
    todo_id = get_id()
    with open(TODO_FILE, 'a') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow([todo_id, title, content, 'false', due])


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


