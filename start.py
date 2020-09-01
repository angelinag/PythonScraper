from Fetch import Fetch
from Parse import Parse

f1 = Fetch()
p1 = Parse(f1.fetchdom())

print(p1.getstars())
print(p1.getnames())
print(p1.gettexts())
print(p1.getdates())

