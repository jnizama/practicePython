
#function using dictionary

d = {} # it could be declare as "d = dict()"

num = input("Enter dimension of dictionary")
n = int(num)
for x in range(1,n+1):
    d[x] = x*x  # not append because it is dictionary not List structure

print(d)

max = 100
for w in range(1,max,3):
    print(w)
    