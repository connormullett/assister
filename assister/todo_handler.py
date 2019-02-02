
import sys
import os
import csv
import pandas as pd

TODO_FILE = os.path.dirname(__file__) + '/todo.csv'


def todo_create():

    while True:
        title = input('Enter title( max 20 )\n>>> ')
        if len(title) > 20:
            continue
        else:
            break
    while True:
        content = input('Enter Content ( max 50 )\n>>> ')
        if len(content) > 50:
            continue
        else:
            break
    while True:
        due = input('Enter due date ( yy/mm/dd )\n>>> ')
        _ = due.split('/')
        i = [int(a) for a in _]
        for d in i:
            if len(str(abs(d))) != 2:
                continue
        if i[1] > 12:
            continue
        if i[2] > 31:
            continue
        break

    f = open(TODO_FILE, 'a')
    writer = csv.writer(f, delimiter=',')
    writer.writerow([title, content, 'false', due])
    sys.stdout.write('todo created successfully\n')
    f.close()


def view_todos():
    f = pd.read_csv(TODO_FILE, 'r', delimiter=',')
    df = pd.DataFrame(f)
    print(df.to_string())


def todo_delete():
    print('gonna delete something')


def todo_router(t):

    if t.lower() == 'create':
        todo_create()

    elif t.lower() == 'del':
        todo_delete()

    elif t.lower() == 'update':
        pass

    elif t.lower() == 'mc':
        pass

    elif t.lower() == 'mi':
        pass

    elif t.lower() == 'cdue':
        pass

    elif t.lower() == 'view':
        view_todos()

    elif t.lower() == 'get':
        pass

    else:
        print('unknown argument')


