#using while

x = 7
while(x > 0):
    print("number is: " + str(x))
    x = x - 1

#while True:
#    pass;

## using IN to evaluating whether exist a value. (it's not like %__% in betweeen SQL but is good to compare values)
r = input("Enter you name")
if(r in 'niza'):
    print('containt niza word')
if(r in ('ox','0','amber','aberico')):
    print('containt |ox|0|amber|aberico word')

#print (str1, str2, str3, ...)  = output => str1 + str2, str3 (concating)
