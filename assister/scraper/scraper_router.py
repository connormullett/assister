
import requests
import sys

from tqdm import tqdm
from bs4 import BeautifulSoup
from .scraper_service import ScraperService


class ScraperRouter:

    def __init__(self, a):
        self.command = a[0]
        self.url = a[1]

    def __call__(self):
        s = ScraperService(self.url)
        s(self.command)

