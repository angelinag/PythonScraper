import re


class Parse:
    def __init__(self, dom):
        self.dom = dom

    def getstars(self):
        stars = self.dom.find_all("div", attrs={"aria-label": re.compile("star rating")})
        ratings = []
        for rating in stars:
            ratings.append(rating['aria-label'])
        del ratings[0]
        print("length of ratings: ")
        print(len(ratings))
        return ratings

    def getnames(self):
        namedata = self.dom.find_all("div", attrs={"role": "region", "aria-label": re.compile(".")})
        names = []
        for name in namedata:
            names.append(name['aria-label'])
        print("length of names: ")
        print(len(names))
        return names

    def gettexts(self):
        namedata = self.dom.find_all("span", attrs={"lang": "en"})
        texts = []
        for text in namedata:
            texts.append(text.string)
        print("length of texts: ")
        print(len(texts))
        return texts

    def getdates(self):
        dates = []
        for rating in self.dom.find_all("div", attrs={"aria-label": re.compile("star rating")}):
            for child in rating.parent.parent.next_sibling.children:
                dates.append(child.text)
        del dates[0]
        print("length of dates: ")
        print(len(dates))
        return dates
