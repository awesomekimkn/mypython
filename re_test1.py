import re

p = re.compile('*\d')
m = p.match("SW214")
print(m)

