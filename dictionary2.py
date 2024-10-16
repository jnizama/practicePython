# Other way to use import

# from class1 import Person  ------>Correct way to import class!
# person1 = Person()   -------> Correct way to declare class!


import class1
# store objects in a dictionary
person1 = class1.Person()
person2 = class1.Person()
person3 = class1.Person()
animal1 = class1.Animal()
animal2 = class1.Animal()



objPersons = { "Cholovikea1" : person1, "Cholovikea2" : person2, 
                "Animal2" : animal2 }
print(objPersons['Cholovikea2'])

r = "Animal2" in objPersons
print(r)


"""
    Using Classes
"""

class People:
    name = ''
    def __init__(self):
        print("inicializacion")

person1 = People()

