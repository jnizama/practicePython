num = []
for x in range(2000,3201):
    if(x%7 == 0) and (x%5 == 0):
            #multipley by 5 and divisible by 7
            num.append(x)

print(num)