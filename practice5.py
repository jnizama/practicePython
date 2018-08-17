def factorial(DieNumber):
    factor = 1;
    for x in range(1,int(DieNumber)):
        factor = factor + (factor * x)
    return factor;

row = ["Dwa", "Trze", "Sztary", "Pienz"]
for r in row:
    print(r)

# Calculate a factorial of a number
#numbers = []
DieNumber = input("Enter number for find its factorial: ")
factorial = factorial(DieNumber)
print(factorial)

