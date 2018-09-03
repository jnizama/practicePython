#using time functions

from time import gmtime
from functionsMain import squareRoot

v = input("Enter number")
r = squareRoot(int(v))
print("SQRT is: " + str(r))

t = gmtime();
print('now is: ' + str(t) )

#print(t)