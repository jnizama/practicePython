import re
file = open('regex_sum_2023417.txt')
totals = 0
for row in file:
    row = row.rstrip()
    numbers = re.findall('[0-9]+',row)
    for x in numbers:
        totals = totals + int(x)
print(totals)