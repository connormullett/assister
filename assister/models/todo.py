
import csv
import os.path


class Todo:

    def __init__(self, title, content, due, complete):
        self.title = title
        self.content = content
        self.due = due
        self.complete = complete


class TodoWrapper:

    def read_csv(self):
        f = open(os.path.dirname(__file__) + '/../../todo.csv')
        reader = csv.reader(f, delimiter=',')
        rows = []
        for row in reader:
            row.append(row)
        return rows

    def add_todo(self, todo):
        pass

    def get_todos(self):
        pass

    def get_todo(self, id):
        pass

    def delete_todo(self, id):
        pass

    def update_todo(self, id):
        pass

    def mark_complete(self, id):
        pass

    def mark_incomplete(self, id):
        pass

    def change_due(self, id):
        pass

