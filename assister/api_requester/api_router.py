
from ..base_models import WriteOut
from .api_service import ApiService

class ApiRouter:
    '''
    assister api <method> <base_url> <body> <headers>
    '''

    def __init__(self, a):
        self.a = a

        if len(self.a) == 2:
            self.service = ApiService(self.a[0], self.a[1])
        elif len(self.a) == 3:
            self.service = ApiService(self.a[0], self.a[1], self.a[2])
        elif len(self.a) == 4:
            self.service = ApiService(self.a[0], self.a[1], self.a[2], self.a[3])


    def __call__(self):
        if self.a is None:
            self.w('Use assister -h for commands', 0)
        self.service()


