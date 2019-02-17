
import requests
import sys

from tqdm import tqdm
from bs4 import BeautifulSoup
from scraper_service import ScraperService


class ScraperRouter:

    def __init__(self, command, url):
        self.command = command
        self.url = url

    def __call__(self):
        s = ScraperService(self.url)
        s(self.command)

