import config

from src.Fetch import Fetch
from src.Parse import Parse
from src.Export import Export

pageURL = config.strings["URL"]
f = Fetch(pageURL)
stars = []
names = []
texts = []
dates = []

while True:
    p = Parse(f.fetchdom())
    morestars = p.getstars()
    morenames = p.getnames()
    moretexts = p.gettexts()
    moredates = p.getdates()
    iscomplete = bool(morestars and morenames and moretexts and moredates)
    if iscomplete is False:
        break
    stars = stars + morestars
    names = names + morenames
    texts = texts + moretexts
    dates = dates + moredates

worksheetname = config.strings["worksheetname"]
filename = config.strings["filename"]
filepath = config.strings["filepath"]
e1 = Export(worksheetname, filename, filepath)
e1.populatecolumn(stars)
e1.populatecolumn(names)
e1.populatecolumn(texts)
e1.populatecolumn(dates)
e1.endexport()
