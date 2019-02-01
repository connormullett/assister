
import csv
import os.path


class Todo:

    def __init__(self, title, content, due, complete):
        self.title = title
        self.content = content
        self.due = due
        self.complete = complete

