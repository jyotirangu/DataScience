# 1	What is aliasing?
# 2	What is garbage collection?
# 3	What is mutability and why is it dangerous in certain scenarios?
# 4	What is cloning?
# 5	Differentiate between deep and shallow copies
# 6	How nested lists are stored in memory?
# 7	How strings are stored in memory
# 8	Why tuples take less memory than lists?
# 9	How set index position is decided?
# 10 Why mutable types are not allowed in sets/dicts

a = 4
id(a)
id(4)
b=a
print(id(a))
print(id(b))

c = b
print(id(c))

del a     

print(b)

a = 'DSMP 2022-23'
b = a
c = b

import sys
sys.getrefcount('DSMP 2022-23')


L = [1,2,3]
print(id(L))

L.append(4)
print(L)
print(id(L))

T = (1,2,3)
print(id(T))

T = T + (4,)

print(T)
print(id(T))

a = [1,2,3]
b = a

b.append(4)
print(b)

print(a)


def func(data):
      data.append(4)

a = [1,2,3]
func(a[:])
print(a)

# cloning
b = a[:]

id(a)
id(b)
b.append(4)
b               # [1, 2, 3, 4]
a               # [1, 2, 3]

a = [1,2,3]
# shallow
b = a.copy()

b.append(4)

print(a)
print(b)

a = [1,2,3,[4,5]]
a                   # [1, 2, 3, [4, 5]]


print(id(a[-1]))        # 139652074560480
print(id(b[-1]))        # 139652074560480

b = a.copy()
b                       # [1, 2, 3, [4, 5]]

print(id(a))            # 139652074868240
print(id(b))            # 139652074561280

b[-1][0] = 400
print(b)

# output : [1, 2, 3, [400, 5]]

a

# output : [1, 2, 3, [400, 5]]


import copy

a = [1,2,3,[4,5]]
a

# output : [1, 2, 3, [4, 5]]

b = a[:]
b

# output : [1, 2, 3, [4, 5]]

b[-1][0] = 400
b

# output : [1, 2, 3, [400, 5]]

a

# output : [1, 2, 3, [400, 5]]

print(id(a[-1]))
print(id(b[-1]))

# output:
# 139652075071600
# 139652074658464

# [:] -> shallow copy

s = 'hello'

id(s)

# output: 139652297075120

id(s[0])

# output: 139652626357424

id('h')

# output: 139652626357424