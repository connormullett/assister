
class Todo:

    def __init__(self, title, content, complete, due):
        self.title = title
        self.content = content
        self.complete = complete
        self.due = due

    def __repr__(self):
        if self.complete:
            status = 'Complete'
        else:
            status = 'Incomplete'
        return self.title, self.content, status, self.due

