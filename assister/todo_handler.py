
import sys
import os
import csv
import pandas as pd
import pkg_resources



# MAKE THIS A CLASS, __del__ maybe and __add__


class WriteOut:
    '''use stdout to write to the console'''
    def __init__():
        pass

    def write_error(self, err):
        sys.stdout.write(err)
        sys.exit(1)

    def write_success(self, msg):
        sys.stdout.write(msg)
        sys.exit(0)


class ReadOut:

    def reader(self, msg):
        i = input(msg)
        return i


class TodoService:

    def __init__(self):
        path = 'todo.csv'
        self.todo_file = pkg_resources.resource_filename(__name__, path)
        print(self.todo_file)

    # This needs to not have any input or stdout
    # for testing reasons
    def todo_create(self):

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

        f = open(self.todo_file, 'a')
        writer = csv.writer(f, delimiter=',')
        writer.writerow([title, content, 'false', due])
        sys.stdout.write('todo created successfully\n')
        f.close()


    def read_todos(self):
        f = pd.read_csv(self.todo_file, 'r', delimiter=',')
        df = pd.DataFrame(f)
        return df


    # Need a todo Class for __repr__ and potential formatting, would b ez
    def view_todos(self):
        df = self.read_todos()
        if not df.empty:
            print(df.to_string())
        else:
            print('No Todos')


    def todo_delete(self, t):

        df = read_todos()
        try:
            i = int(t)
        except Exception:
            print('{} is not a valid row identifier'.format(t))
            sys.exit(0)

        try:
            print(df.iloc[i].to_string())
            choice = input('are you sure you want to delete this todo? (y/n)\n')
        except Exception:
            sys.stdout.write('Invalid ID\n')
            sys.exit(0)
        if choice.lower() == 'n':
            sys.exit(0)
        elif choice.lower() == 'y':
            with open(self.todo_file, 'r') as f:
                rows = f.readlines()
                del rows[i + 1]

            with open(self.todo_file, 'w') as f:
                for row in rows:
                    f.write(row)
            sys.stdout.write('Todo Deleted Successfully\n')


class TodoRouter():

    def __init__(self, t):
        self.t = t
        self.service = TodoService()

    def __call__(self):
        if len(self.t) > 1:
            self.todo_arg_router()
        else:
            self.router(self.t[0])


    # Refactor to function map indexing
    # if a in arg_router_map ... where map is a dict
    def router(self, a):
        if a == 'create':
            self.service.todo_create()
        elif a == 'view':
            self.service.view_todos()
        elif a == 'reset':
            # TODO: os.system( run install.sh )
            pass
        else:
            print('Unknown argument\n' +
                  'Use assister -h for commands')

    def todo_arg_router(self):
        if self.t[0] == 'del':
            self.service.todo_delete(selft[1])
        elif self.t[0] == 'mi':
            pass
        elif self.t[0] == 'mc':
            pass
        elif self.t[0] == 'cdue':
            pass
        elif self.t[0] == 'update':
            pass
        else:
            print('unknown argument\n' +
                  'Use assister -h for commands')

