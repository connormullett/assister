
import requests
from ..base_models import WriteOut, ReadOut

class ApiService:

    def __init__(self):
        self.w = WriteOut()
        self.r = ReadOut()

    def __call__(self, request_method, base_url):
        if request_method.lower() == 'get':
            response = requests.get(base_url)
            self.w(response.text, 0)

