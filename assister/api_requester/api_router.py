
from ..base_models import WriteOut
from .api_service import ApiService

class ApiRouter:
    '''
    assister --api get <base_url> <api_key>
    '''

    def __init__(self, a):
        self.a = a
        self.service = ApiService(self.a[0], self.a[1])


    def __call__(self):
        if self.a is None:
            self.w('Use assister -h for commands', 0)
        self.service()


