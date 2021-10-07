import math
y = 2
x = 5
z = x + y
print(z)
print(z/x)
print(z//x)
print(10%3)
print('Marcos\'s "laptop" ')
print(r'c:\docs\MARCOS')
name = 'MARCOS'
print(name[2])
print(name[-1])
print(name[-2])
print(name[1:3])
print(name[:3])
print(name[3:])
print(len(name))
nums = [5, 4, 6, 7]
names = ['Marcos', 'Deicy', 'Jose', 'Luis']
mil = [nums, names]

print(nums)
print(nums[2])
print(nums[:2])
print(nums[2:])
print(mil)
nums.append(55)
nums.insert(3, 75)
print(nums)
nums.remove(4)
print(nums)
nums.pop(2)
print(nums)
del nums[:2]
print(nums)
nums.extend([2, 5, 6, 7])
print(nums)
print(sum(nums))
print(max(nums))
nums.sort()
print(nums)
tup = (5,6, 8)
print(tup)
data = { 1:'marcos', 2:'Deicy', 4:'jose'}
print(data)
print(data[4])
print(data.get(2))
print(data.get(3, 'no fund'))
names = ['Marcos', 'Deicy', 'Jose', 'Luis']
mil = [nums, names]
data2 = dict(zip(nums, names))
print(data2)
data3 = { 1:'marcos', 2:['Deicy', 'Tata'], 4: {'jose':'desgin', 'Maya':'Counter'}}
print(data3)
print(data3[1])
print(data3[2])
print(data3[2][0])
print(data3[4]['Maya'])
print(id(x))
print(type(x))
f = float(x)
print(type(f))
print(list(range(10)))
print(list(range(2,10,2)))
print(x<y)
print(math.sqrt(9))
In = int(input("is a even or odd"))

print(In % 2 == 0)
ch = input("Intdus a p")[0]
print(ch)

data = ['marcos', 0, 5, 'l']
for i in data:
    print(i)

for i in range(4):
    if i > 2:
        print('out of stocks')
        break
    if i == 1:
        print('Continue')
        continue
    print(data[i])