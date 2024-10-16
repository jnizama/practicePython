# Las funciones map() y filter() en Python son herramientas muy útiles 
# para trabajar con iterables. 
# Permiten aplicar funciones a elementos de listas, tuplas y otros objetos iterables 
# de manera concisa y eficiente. 


numeros = [1,2,3]
x = 0
myMapa = map(lambda x: x ** 2 , numeros)

# print all numbers divisible by 7 (USING "FILTER")

divNumber = range(1,100)
divBy7 = filter(lambda r: r%7 == 0, divNumber)
for l in divBy7:
    print(l)