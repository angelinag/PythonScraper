from src.Fetch import Fetch
from src.Parse import Parse
from src.Export import Export

f = Fetch()
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


e1 = Export()
e1.populatecolumn(stars)
e1.populatecolumn(names)
e1.populatecolumn(texts)
e1.populatecolumn(dates)
e1.endexport()
