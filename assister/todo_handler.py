
import sys
import os
import csv
import pandas as pd
import pkg_resources
import time

from datetime import datetime


class WriteOut:

    def __call__(self, msg, code=None):
        sys.stdout.write(msg + '\n')
        if code is 0 or code:
            sys.exit(code)


class Todo:

    def __init__(self, title, content, complete, due: str):
        self.title = title
        self.content = content
        self.complete = complete
        self.due = due

    def __repr__(self):
        # TODO: reformat timestamp to datetime
        return (self.title, self.content, self.complete, time.ctime(self.due))


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

        # TODO: Add handling for dates with errors
        due = self.r('Enter due date (DD/MM/YYYY)')

        try:
            with open(self.todo_file, 'a') as f:
                t = Todo(title, content, False, due)
                writer = csv.writer(f, delimiter=',')
                writer.writerow(t.__repr__())
                self.w('Todo created successfully', 0)
                f.close()
        except Exception:
            self.w('An Error has occured\nReinstall the program or run reset', 1)


    def read_todos(self):
        with open(self.todo_file, 'r') as f:
            _ = f.readlines()
            todos = []
            del _[0]
            for todo in _:
                todo = todo.rstrip()
                todos.append(todo)
            return todos


    def view_todos(self):
        todos = self.read_todos()
        # TODO: Print todos from objects
        for todo in todos:
            t = todo.__repr__().split(',')
            t[0] = t[0].replace("'", '')
            t[-1] = t[-1].replace("'", '')

            print(t)
        self.w('', 0)

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
        self.w = WriteOut()

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
        except Exception as e:
            self.w('An Error Occured, {}'.format(e), 1)
        self.w('No Command Found\n' +
               'Use -h for help', 0)

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

