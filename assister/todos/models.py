
class Todo:

    def __init__(self, title, content, complete, due):
        self.title = title
        self.content = content
        self.complete = complete
        self.due = due

    def __repr__(self):
        return self.title, self.content, self.complete, self.due

