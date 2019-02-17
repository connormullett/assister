
import requests
import sys

from bs4 import BeatifulSoup
from tqdm import tqdm
from ..base_models import WriteOut


class ScraperService:
    '''
    usage: `ass scrape <text/http-links/links> <url>`
    '''

    def __init__(self, url):
        response = requests.get(url)
        self.b = BeautifulSoup(response.text, features='html.parser')
        self.w = WriteOut()

        self.command_mapper = {
                    'links': self.get_links,
                    'http-links': self.get_http_links,
                    'text': self.get_text
                }

    def __call__(self, command):
        c = self.command_mapper.get(command, None)
        if c is None:
            self.w('Unknown command: ' + command, 1)
        c()

    def get_http_links(self):
        links = []
        for link in tqdm(self.b.find_all('a')):
            if link.get('href').startswith('http'):
                links.append(link.get('href'))
        for link in links:
            self.w(link)

    def get_links(self):
        links = []
        for link in tqdm(self.b.find_all('a')):
            links.append(link.get('href'))
        for link in links:
            self.w(link)

    def get_text(self):
        self.w(self.b.get_text())

