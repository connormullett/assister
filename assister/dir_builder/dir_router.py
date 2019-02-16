
import os
from .dir_service import DirectoryService


class DirectoryRouter:

    def __init__(self, a: list):
        self.a = a
        self.service = DirectoryService(a)

    def __call__(self):
        self.service()

