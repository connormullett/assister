
import os
import time

from tqdm import tqdm


class DirectoryService:

    def __init__(self, args: list):
        self.args = args

    def __call__(self):
        path = os.getcwd()
        if not self.args[0].startswith('/'):
            self.args[0] = f'/{self.args[0]}'
        os.makedirs(f'{path}{self.args[0]}')
        for i in tqdm(self.args[1:]):
            if not i.startswith('/'):
                i = f'/{i}'
            open(path + self.args[0] + i, 'w').close()
            time.sleep(0.1)

