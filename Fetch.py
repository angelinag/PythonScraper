import requests
from bs4 import BeautifulSoup


class Fetch:
    def __init__(self):
        self.URL = 'https://www.yelp.com/biz/american-airlines-irving'

    def fetchdom(self):
        page = requests.get(self.URL)
        return BeautifulSoup(page.content, 'html.parser')
