## functions strings
import sys
import os

os.system('cls')
nameOf = "Joseph Flaw"
print(nameOf[0])
print(nameOf[:10])   # ----> not include position 10 in the string

name = "Mathew's our \"friend\" "
print(name)

#using three quotes
word1 = """ Co to 
        jest gdie ty jest
        noc """

        
print(word1)

strname = "the number of cars is "
strname = strname + str(17)
print(strname)

sys.exit()  #--> exit of the program

#split
address = "Av. San Jose de Obregon 123"
splitAddress = address.split() ##split in list objects
print(splitAddress)
## result
## ['Av.', 'San', 'Jose', 'de', 'Obregon', '123']

# Limiting characteres for strings
file = open("numCholoviekas.txt")
with file as f:
    row = f.readline()
    arrayRow = row.split("\t")
    for r in arrayRow:
            name = arrayRow[0]
            weight = arrayRow[1]
            age = arrayRow[2]
print(name)
print(weight)
print(age)
file.close()

#convert integer to string
PI = 3.1416
print("PI Number value is: " + str(PI))