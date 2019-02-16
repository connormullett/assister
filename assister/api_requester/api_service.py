
import requests
import json
from ..base_models import WriteOut, ReadOut

class ApiService:

    def __init__(self, request_method, url, headers=None):
        self.w = WriteOut()
        self.r = ReadOut()

        self.request_method = request_method
        self.url = url

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
        response = requests.get(self.url)
        try:
            r = json.loads(response.text)
            self.w(json.dumps(r, indent=4, sort_keys=True), 0)
        except json.decoder.JSONDecodeError:
            self.w(response.text)


    def post(self):
        pass

    def delete(self):
        pass

    def put(self):
        pass

