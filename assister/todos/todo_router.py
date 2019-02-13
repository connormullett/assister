
from ..base_models import WriteOut
from .todo_service import TodoService

class TodoRouter():

    def __init__(self, t):
        self.t = t
        self.service = TodoService()
        self.w = WriteOut()

    def __call__(self):
        if self.t is None:
            self.w('Use assister -h for commands', 0)
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

    def todo_arg_router(self):
        function_mapper = {
                    'del': self.service.todo_delete,
                    'mc': self.service.mark_complete,
                    'mi': self.service.mark_incomplete,
                    'cdue': self.service.change_due,
                    'update': self.service.todo_update
                }
        b = function_mapper[self.t[0]]
        b(self.t[1])

