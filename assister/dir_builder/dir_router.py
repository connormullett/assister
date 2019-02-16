
import sys
from dir_service import DirectoryService


class DirectoryRouter:

    def __init__(self, a):
        self.a = a
        self.service = DirectoryService()
        # TODO: plan arguments for directory builder

    def __call__(self):
        pass

