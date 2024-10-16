import re

#This is the best way to scan files line by line bc not print new line empty
file = open('stringsPy.txt')
for line in file:
  line = line.rstrip()
  if(re.search('From', line)):
     print(line)


for line in file:
  line = line.rstrip()
# This RE seek only From starting in the line (not in middle or least line)
# TRUE if from come in the beginning of the line or FALSE other case
  if(re.search('^From:', line)):
     print(line)

