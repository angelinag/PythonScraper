import requests
from bs4 import BeautifulSoup


class Fetch:
    def __init__(self):
        self.URL = 'https://www.yelp.com/biz/american-airlines-irving'
        self.pagenum = 0

    def getnextpageurl(self):
        querystring = '?start=' + str(self.pagenum * 20)
        self.pagenum = self.pagenum + 1
        return self.URL + querystring

    def fetchdom(self):
        page = requests.get(self.getnextpageurl())
        return BeautifulSoup(page.content, 'html.parser')
