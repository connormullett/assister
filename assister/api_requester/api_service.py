
import requests
from ..base_models import WriteOut, ReadOut

class ApiService:

    def __init__(self, request_method, base_url, headers=None):
        self.w = WriteOut()
        self.r = ReadOut()

        self.request_method = request_method
        self.base_url = base_url

        if headers:
            self.headers = headers

    def __call__(self):

        method_mapper = {
                    'get': self.get,
                    'post': self.post,
                    'del': self.delete,
                    'put': self.put
                }

        m = method_mapper[self.request_method]
        m()

    def get(self):
        pass

    def post(self):
        pass

    def delete(self):
        pass

    def put(self):
        pass

