#!/usr/bin/python

#Belgium string
Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

hyphens = '-' * len(Belgium)
print(hyphens)

#Change , to : using .replace
belgium_colons = Belgium.replace(',', ':')
print(belgium_colons)

#Created an integer for Belgium value
fields = Belgium.split(',')
a = int(fields[1])

#Created an integer for Brussel's value
b = int(fields[3])

#created a numerical string to add the two values together
c = a + b
print(c)
