
import requests
import json
from ..base_models import WriteOut, ReadOut

class ApiService:

    def __init__(self, request_method, url, body=None, headers=None):
        self.w = WriteOut()
        self.r = ReadOut()

        self.request_method = request_method
        self.url = url

        if headers:
            self.headers = headers
        if body:
            self.body = body

    def __call__(self):

        # TODO: Add header Functionality for Post, Put, and Del methods
        method_mapper = {
                    'get': self.get,
                    'post': self.post,
                    'del': self.delete,
                    'put': self.put
                }

        m = method_mapper[self.request_method]
        m()

    def wrap_json(response):
        try:
            r = json.loads(response.text)
            self.w(json.dumps(r, indent=4, sort_keys=True), 0)
        except json.decoder.JSONDecodeError:
            self.w(response.text, 0)

    def get(self):
        if not self.headers:
            response = requests.get(self.url)
        else:
            response = requests.get(self.url, headers=self.headers)
        wrap_json(response)


    def post(self):
        response = requests.post(self.url, data='{}'.format(self.body))
        self.w(str(response), 0)

    def delete(self):
        response = requests.delete(self.url)
        self.w(str(response), 0)

    def put(self):
        response = requests.put(self.url, data='{}'.format(self.body))
        self.w(str(response), 0)

