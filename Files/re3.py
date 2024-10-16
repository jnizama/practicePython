import re

file = open('stringsPy.txt')
## This RE print all lines that have numbers in array format
for line in file:
  line = line.rstrip()
  numbers = re.findall('[0-9]+', line)
  print(numbers) 


cadena = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
seek = re.findall('\S+?@\S+', cadena)
print(seek)

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)

y = 'asfasf asf 854 5 asf. @85'
seek = re.findall('[a-z0-9]', cadena)
print(seek)