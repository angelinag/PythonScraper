import requests
from bs4 import BeautifulSoup


class Fetch:
    def __init__(self, URL):
        self.URL = URL
        self.pagenum = 0

    def getnextpageurl(self):
        querystring = '?start=' + str(self.pagenum * 20)
        self.pagenum = self.pagenum + 1
        return self.URL + querystring

    def fetchdom(self):
        page = requests.get(self.getnextpageurl())
        return BeautifulSoup(page.content, 'html.parser')
