import os
import sys

os.system("cls")

customers1 = ["John", "Peter", "Paul", "Robert", "Luis"]
customers1.insert(2, "Nora")
print(customers1)

customers2 = ["Kasandra", "Sara", "Jorge", "Marie"]
customers1 = customers1 + customers2
print(customers1)

dato = "Saras" in customers2
print(dato)



# itering in a basic collection with for and if 
nombres = ["sin","cos","tag","ctag"]
print("hello")
for n in nombres:
    if n == "cos":
        print("Es coseno " + n)
    else:
        print(n)

#hadling Sliced List.
print(nombres[2:])

#add values to List
nombres.append("sec")
nombres.append("csec")
print(nombres[:])
##show whole methods of List
print(dir(nombres))

##ordering a List
nombres.sort()
print(nombres)

## adding list from the scratch
courses = list()
courses.append("Math")
courses.append("Physic")
courses.append("Mechanikal")
print(courses)
## check whethers is some in a List
existMaht = "Math" in courses
if(existMaht):
    print('Math was added')
else:
    print('Math was not added')
## math operation on List
first5Impars = [1,3,5,7,9]
totalSum5Impars = sum(first5Impars)
print(totalSum5Impars)

impart = 9%2
if(impart > 0):
    print('numero impar')
else:
    print('numero par')