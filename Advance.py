import math
from numpy import *
def fun(a, b):
    pass
glob = 10
def greet(A,b):
    print('hello', A)
    print('good morrning', b)

def person(name, **data):
    global glob
    glob = 15
    print(data)


for i in range(5):
    for x in range(i+1):
        print('#', end="")
    print()
nums = [67, 19, 46, 59]
for i in nums:
    if(i % 5 == 0):
        print(i)
        break
else:
    print("no found")

num = 5
for i in range(2, num):
    if num % i == 0:
        print("it is not prime")
        break
else:
    print("it is prime")

vals = array([1,2,4])
vals2 = array([1,2,4])
print(vals[1])
vals = vals + 5
val3 =  vals + vals2
print(vals)
print(val3)
matriz = array([
    [1,2,3],
    [4,5,6]
])

m = matrix(matriz)
print(matriz.size,  " ", matriz.ndim ," ", matriz.shape)
print(m)
greet(4,5)
person('marcos', type='student', age=28)
print(glob)

lst = [1,2,3,4,5,6,7,8,9]
def CountEvensandOdds(lst):
    even = 0
    odd = 0
    for l in lst:
        if l%2==0:
            even+=1
        else:
            odd+=1
    return even, odd
evens, odds= CountEvensandOdds(lst)
print('Even: {}, odd: {}'.format(evens, odds))

evn = list(filter(lambda n : n%2 == 0, lst))
print(evn)