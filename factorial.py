def facto(num):
    result = 1
    for x in range(1,num+1):
        result = result * x
        #print(x)
    return result

#compute factorial
num = input("enter number")
try:
    i = int(num)
    if type(i) == int:
        f = facto(i)
    else:
        print("value not valid")
    
    print(f)
except ValueError:
    print("input value not valid")

#another way to validating number
# num = input("enter number")
# i = int(num)
# if type(i) == int:
#     f = facto(i)
# else:
#     print("value not valid")    
# print(f)
