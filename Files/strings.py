file = open('stringsPy.txt')
for line in file:
  if(line.find('From') >= 0):
     print(line)
