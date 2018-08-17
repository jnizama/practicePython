
#COMIENZO
print ("hola mundo")

#type ---> DataType
print (type("hola"))
print (type(12.222))
print(type('demo'))
print(type(False))
print(type(True))
print("*" * 45)  #multiplica 45 veces el asterisco
print("I am " + str(12) + " years old") #convertir valores enteros a string

print(int("12")) #convertir caracter a numerico
print(float(3)) # convierte el entero a float
print(bool("")) # si no hay nada lo pone a FALSE de lo contrario siempr devolvera TRUE
print(bool("A"))

# VARIABLES

valor = 12
mark = "Mark have " + str(valor)
print(mark)
#always named first letter of valiables with underling or letters


print ("hola","mujer","hermosa") # concatena estas 3 palabras con un espacio en cada una
#PRINT end
print ("Demo", end=" ") # evita hacer la nueva linea y lo muestra como una sola
print("remdio") # Esto imprime Demo remdio en una sóla línea.

#PRINT dep
print ("hola","mujer","hermosa",sep="...") #en vez de sapararlo por un espacio los separa por tres puntos

#INPUT (ASK TO USER TO INPUT SOMETHING)
nombre = input("cual es tu nombre:"); #Este texto es opcional pero ayuda al usuario que escriba algo el usuario
print(nombre)
#INPUT devuelve una referencia a la variable de tipo STR
age = int(input("How old are you: "))
print(age)

#NOT (negacion logica), AND , OR(true cuando al menos unos de los operadores es true)

#IF...
if age >= 20:
    print("eres mas de 20")
else:
    print("eres menor de 20")

flag = True
if(flag) :
    print("El fla es true")

#Elif
flag = False
if(flag) :
    print("El fla es true")
elif(not flag):
    print("El fla es false")