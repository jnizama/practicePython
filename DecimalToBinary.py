binaryNumber = []

def convertToBinary(iNumber:int):
    resto = round(iNumber%2);
    binaryNumber.append(resto)
    iNumber = int(iNumber/2)
    if(iNumber > 1):
        convertToBinary(iNumber)
    else:
        binaryNumber.append(iNumber)
    #for x in range(iNumber, 0,-1):
    #    print(x)
    binaryNumber.reverse()
    
    

print("Conversion Decimal to Binary")

iNumber = input("Enter the number")
TheNumber = int(iNumber)
convertToBinary(TheNumber)
print(binaryNumber);
#print(str(int(5/2)));