#read file
#with is a Python's keyword similarly to using in C# to work with unmanaged resource
import sys

file = open('example.txt')
with open('example.txt') as f:
    for x in f:
        print(x)

file.close()

#with expression [as variable]:
#   with-block