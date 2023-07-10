#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
hyphens = '-' * len(Belgium)
print(hyphens)
belgium_colons = Belgium.replace(',', ':')
print(belgium_colons)

fields = Belgium.split(',')
a = int(fields[1])
print(a)

b = int(fields[3])
print(b)

c = a + b
print(c)