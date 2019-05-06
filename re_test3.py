import re

#p = re.compile('\w*\(a.b\)\w*')
q = re.compile('\(\w*\)')
#m = p.match("w(a234dfasghadsfsb)zz")
m = q.findall("asdfasdw(a982134_aljkdsfsb)11213zz")
print(m)

