
import sys
import os
import csv
import pkg_resources
import time

from ..base_models import WriteOut, ReadOut
from .models import Todo
from datetime import datetime


class TodoService:

    def __init__(self):
        path = 'todo.csv'
        self.todo_file = pkg_resources.resource_filename(__name__, path)
        self.r = ReadOut()
        self.w = WriteOut()

    def mark_complete(self, todo_id):
        todos = self.read_todos()
        todo_str = todos[int(todo_id)]
        title, content, complete, due = todo_str.split(',')
        todo = Todo(title, content, bool(complete), due)
        todo.complete = True
        self.w('Todo marked complete')
        self.delete_row(int(todo_id))
        self.write_row(todo)

    def mark_incomplete(self, todo_id):
        todos = self.read_todos()
        todo_str = todos[int(todo_id)]
        title, content, complete, due = todo_str.split(',')
        todo = Todo(title, content, bool(complete), due)
        todo.complete = False
        self.delete_row(int(todo_id))
        print(todo.__repr__())
        self.write_row(todo)

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
        t = Todo(title, content, False, due)
        self.write_row(t)

    def write_row(self, t):
        with open(self.todo_file, 'a') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow(t.__repr__())


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
        for i, todo in enumerate(todos):
            t = todo.__repr__().split(',')
            t[0] = t[0].replace("'", '')
            t[-1] = t[-1].replace("'", '')
            self.w(f'{i}\t{t[0]}\t{t[1]}\t\t{t[2]}\t{t[3]}')
        self.w('', 0)

    def todo_delete(self, t):

        todos = self.read_todos()
        i = int(t)

        self.w(todos[i])
        try:
            choice = self.r('are you sure you want to delete this todo? (y/n)')
        except Exception as e:
            self.w('Invalid ID\n', 1)
        if choice.lower() == 'n':
            sys.exit(0)
        elif choice.lower() == 'y':
            self.delete_row(i)

    def change_due(self):
        pass

    def todo_update(self):
        pass

    def delete_row(self, i):
        with open(self.todo_file, 'r') as f:
            rows = f.readlines()
            del rows[i + 1]

        with open(self.todo_file, 'w') as f:
            for row in rows:
                f.write(row)

