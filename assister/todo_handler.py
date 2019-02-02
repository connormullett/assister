
import sys
import os
import csv
import pandas as pd

TODO_FILE = os.path.dirname(__file__) + '/todo.csv'


def get_rows():
    # TODO: refactor this for pandas
    f = open(TODO_FILE)
    reader = csv.reader(f, delimiter=',')
    rows = []
    for row in reader:
        rows.append(row)
    return rows
    f.close()


def get_id():
    # this is garbage im sorry
    rows = get_rows()
    _ = []
    for row in rows:
        _.append(row[0])
    del _[0]
    if len(rows) == 1:
        return 1
    todos = []
    for i in _:
        a = int(i)
        todos.append(a)

    return next(a for a, b in enumerate(todos, (len(todos) + 1)) if a != b)


def todo_create():

    # TODO: horribly hard coded, gonna create a month wrapper
    # for the monstrosity on 53
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
    todo_id = get_id()

    f = open(TODO_FILE, 'a')
    writer = csv.writer(f, delimiter=',')
    writer.writerow([todo_id, title, content, 'false', due])
    f.close()


def view_todos():
    f = pd.read_csv(TODO_FILE, 'r')
    # for row in f.readlines():
    #     print(row.strip('\n'))
    df = pd.DataFrame(f)
    print(df)


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
        view_todos()

    elif t.lower() == 'get':
        pass

    else:
        print('unknown argument')


