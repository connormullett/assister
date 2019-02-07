
import sys
import os
import csv
import pandas as pd
import pkg_resources
# TODO: Refactor to remove Pandas

class WriteOut:

    def __call__(self, msg, code):
        sys.stdout.write(msg + '\n')
        sys.exit(code)


class ReadOut:

    def __call__(self, msg):
        i = input(msg + '\n>>> ')
        return i


class TodoService:

    def __init__(self):
        path = 'todo.csv'
        self.todo_file = pkg_resources.resource_filename(__name__, path)
        self.r = ReadOut()
        self.w = WriteOut()

    def todo_create(self):

        while True:
            title = self.r('Enter title (max 20 characters)')
            if len(title) > 20:
                continue
            else:
                break
        while True:
            content = self.r('Enter todo body (max 50 characters)')
            if len(content) > 50:
                continue
            else:
                break
        while True:
            due = self.r('Enter due date (YY/MM/DD)')
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

        try:
            f = open(self.todo_file, 'a')
            writer = csv.writer(f, delimiter=',')
            writer.writerow([title, content, 'false', due])
            self.w('Todo created successfully', 0)
            f.close()
        except Exception:
            self.w('An Error has occured\nReinstall the program or run reset', 1)


    def read_todos(self):
        f = pd.read_csv(self.todo_file, 'r', delimiter=',')
        df = pd.DataFrame(f)
        return df


    # Need a todo Class for __repr__ and potential formatting, would b ez
    def view_todos(self):
        df = self.read_todos()
        if not df.empty:
            self.w(df.to_string(), 0)
        else:
            self.w('No Todos', 0)


    def todo_delete(self, t):

        df = self.read_todos()
        try:
            i = int(t)
        except Exception:
            print('{} is not a valid row identifier'.format(t))
            sys.exit(0)

        try:
            print(df.iloc[i].to_string())
            choice = self.r('are you sure you want to delete this todo? (y/n)')
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

    def router(self, a):
        function_mapper = {
                    'create': self.service.todo_create,
                    'view': self.service.view_todos,
                }
        try:
            b = function_mapper[a]
            b()
        except Exception:
            print('Unknown argument\n' +
                  'Use assister -h for commands')

    def todo_arg_router(self):
        function_mapper = {
                    'del': self.service.todo_delete,
                    # mi, update, mc, cdue
                }
        try:
            b = function_mapper[self.t[0]]
            b(self.t[1])
        except Exception:
            print('unknown argument\n' +
                  'Use assister -h for commands')

