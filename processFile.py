# This example compute IMC from 10 persons according their weight & size

class Agente:
   """A SIMPLE EXAMPLE""" #docstring belonging to the class
   age = 7
   def __init__(self, LineFile, Name,Weight,Size):
       self.LineFile = LineFile
       self.Name = Name
       self.Weight = Weight
       self.Size = Size
   
def splitLine(agente):
    pos = 0
    limit1 = 0
    limit2 = 0
    limit3 = 0
    for x in line:
        pos = pos + 1
        if x == "\t" and agente.Name == '':
            agente.Name = agente.LineFile[:pos-1]
            limit1 = pos
        elif x == "\t" and agente.Weight == 0:
            agente.weight = agente.LineFile[limit1:pos-1]
            limit2 = pos
        elif x == "\t" and agente.Size == 0:
            agente.size = agente.LineFile[limit2:pos-1]
            limit3 = pos
            
mfile = open("numCholoviekas.txt")
#print(mfile)
with open("numCholoviekas.txt") as f:
    line = f.readline()
    name = ''
    weight = 0
    size = 0
    agente = Agente(line, name, weight, size)
    splitLine(agente)
    print(agente.Name)
    print(agente.age)
    print(agente.__doc__)

mfile.close()

