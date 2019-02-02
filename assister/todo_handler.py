
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


def read_todos():
    f = pd.read_csv(TODO_FILE, 'r', delimiter=',')
    df = pd.DataFrame(f)
    return df


def view_todos():
    df = read_todos()
    print(df.to_string())


def todo_delete(t):
    df = read_todos()
    try:
        i = int(t)
    except Exception:
        print('{} is not a valid row identifier'.format(t))
        sys.exit(1)
    print(df.iloc[i].to_string())
    choice = input('are you sure you want to delete this todo? (y/n)\n')
    if choice.lower() == 'n':
        sys.exit(0)
    elif choice.lower() == 'y':
        f = open(TODO_FILE, 'w')
        # TODO: this crap needs to be in csv format
        f.write(df.drop([0]).to_string())
        sys.stdout.write('Succesfully deleted todo\n')


def todo_router(t):
    ''' handles an integer, or a list as an argument
        then routes accordingly throughout the module '''

    id_option_map = ['del', 'mi', 'mc', 'cdue', 'update']

    # mapper
    if type(t) == str:
        if t in id_option_map:
            sys.stdout.write('No id specified\n')
            sys.exit(0)

    # no args for -t
    if type(t) == str:
        if t.lower() == 'create':
            todo_create()
        elif t.lower() == 'view':
            view_todos()

    # args for -t
    # pass t[1] to these functions
    if type(t) == list:

        if t[0] == 'del':
            todo_delete(t[1])
        elif t[0] == 'mi':
            pass
        elif t[0] == 'mc':
            pass
        elif t[0] == 'cdue':
            pass
        elif t[0] == 'update':
            pass
        else:
            print('unknown argument')

