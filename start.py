from src.Fetch import Fetch
from src.Parse import Parse
from src.Export import Export

f1 = Fetch()
p1 = Parse(f1.fetchdom())

e1 = Export()
e1.populatecolumn(p1.getstars())
e1.populatecolumn(p1.getnames())
e1.populatecolumn(p1.gettexts())
e1.populatecolumn(p1.getdates())
e1.endexport()


