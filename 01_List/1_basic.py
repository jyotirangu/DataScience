#1 A referential array in Python refers to an array-like structure where the array elements hold references to other objects. This means the array stores pointers to the actual data, not the data itself. In Python, all lists and arrays inherently behave this way since Python's variables are references to objects, not the objects themselves.

arr = [1, "hello", [2, 3]]

# Here, arr is a referential array:

# arr[0] points to an integer object 1.
# arr[1] points to a string object "hello".
# arr[2] points to a list object [2, 3].
# The array does not store these objects directly but holds references to where they are stored in memory.

print(id(arr))      #2497280348544
print(id(arr[0]))   #140706622736824
print(id(arr[1]))   #2497280361312
print(id(arr[2]))   #2497280350464


# 2  lists are heterogeneous, meaning they can store elements of different data types in the same list. This allows you to mix integers, strings, floats, objects, or even other lists within a single list structure.


# Characteristics of a List
# 1. Lists are ordered collections of items that can be of any data type, including strings

L1 = [1, 2, 3]
L2 = [3, 2, 1]
print(L1 == L2)     #false

# 2. Changeble/ Mutable
# 3. HEtrogeneous
# 4. Can have duplicates
# 5. Dynamic
# 6. Can be nested
# 7. items can be accessed
# 8. Can contain any kind of objects in python

# Creating a Empty list
print([])

# Creating 1D list  --> Homo
print([1, 2, 3, 4, 5])

# Creating 2D list  --> Hetero
print([1, 2, 3, [4, 5]])

# Creating 3D list --> Homo
print([[[1,2],[3,4]],[[5,6],[7, 8]]])   #It is homogenous, as you considere the last bracket it consist of two lists, and each list consist of two elements

# Heterogenous
print([1, True, 5.6, 5+6j, 'Hello'])

# Using Type Conversion
print(list('hello'))
# The expression list('hello') converts the string 'hello' into a list of its individual characters using type conversion.
# list() function: This function can be used to convert any iterable (like strings, tuples, sets) into a list.


# Accessing items from a List

# 1. Indexing: Accessing items by their index position in the list.
M = [1, 2, 3, [4, 5]]

# Positive indexing
print(M[0])  # Output: 1
print(M[3][0])  # Output: 4

# Negative indexing
print(M[-1])  # Output: [4, 5]
print(M[-1][0])  # Output: 4

N = [[[1,2],[3,4]],[[5,6],[7, 8]]]
print(N[1][0][0]) #Output: 5
print(N[0][0][1]) #Output: 2

# Slicing

print(M[0:])
print(M[0::2])
print(M[-4:-2]) #Output: [1, 2] 
print(M[::-1])  #[[4, 5], 3, 2, 1] Reversing

# Adding items to a list

# 1. Append(): Adds an item to the end of the list.
E = [1, 2, 3, 4, 5]
E.append([True, 6])
print(E)        #output: [1, 2, 3, 4, 5, [True, 6]] used too add only one item at a time, then that item can be a list or any other data type

# 2. Extend()
E.extend([6, 7, 8])
print(E)        #output:[1, 2, 3, 4, 5, True, 6, 7, 8] Used for adding multiple elements

E.extend('Delhi')
print(E)        #[1, 2, 3, 4, 5, [True, 6], 6, 7, 8, 'D', 'e', 'l', 'h', 'i'] Extend wil treat the string as a list of characters, so it always tries to add multiple item out of a string

# E.extend(890)
# print(E)    #TypeError: 'int' object is not iterable

# 3. Insert(): Inserts an item at a specified position in the list.
E.insert(1, 100)
print(E)        # [1, 100, 2, 3, 4, 5, [True, 6], 6, 7, 8, 'D', 'e', 'l', 'h', 'i']


# Editing items in a List

# Editing with index
E[-6] = 800
print(E)        # [1, 100, 2, 3, 4, 5, [True, 6], 6, 7, 800, 'D', 'e', 'l', 'h', 'i']

# Editing with slicing
E[2:5] = [200, 300, 400]
print(E)        # [1, 100, 200, 300, 400, 5, [True, 6], 6, 7, 800, 'D', 'e', 'l', 'h', 'i']

# Deleting items from a List
# del, remove, pop, clear

# del by index
del E[-1]
print(E)   # Output : [1, 100, 200, 300, 400, 5, [True, 6], 6, 7, 800, 'D', 'e', 'l', 'h']

# del by slicing
del E[-4:-1]
print(E)    # Output : [1, 100, 200, 300, 400, 5, [True, 6], 6, 7, 800, 'h']

# remove () by value
E.remove(400)
print(E)    # Output : [1, 100, 200, 300, 5, [True, 6], 6, 7, 800, 'h']

# pop() by index
E.pop(0)
print(E)    # Output : [100, 200, 300, 5, [True, 6], 6, 7, 800, 'h']

E.pop()     # If not provided index by default it will remove the last item
print(E)    # Output : [100, 200, 300, 5, [True, 6], 6, 7, 800] 

# clear
E.clear()
print(E)    # Output : [] does not delete the list, it just removes all the elements from the list. The list still exists in the memory.

# Operations on Lists
# Arithmetic, Membership and Loop

# Arithmetic(+, *)

a = [1, 2, 3]
b = [4, 5, 6]

# Concatenation/Merge
print(a + b)    # Output : [1, 2, 3, 4, 5, 6]

print(a*3)      # Output : [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Membership Operator

print(5 in a)   # Output : False
print(5 not in a) # Output : True

c = [7, 8, [9, 10]]
print(9 in c)     # Output : False

# Loops

for i in c:
    print(i, end = ' ')
print()

d = [[[1,2],[3,4]],[[5,6],[7, 8]]]
for i in d:
    print(i)
    
    
# List Functions

# len/min/max/sorted/

d = [1, 2, 3, 4, 'Delhi']
print(len(d))   # Output : 5
# print(min(d))   # Output : TypeError: '<' not supported between instances of 'str' and 'int'
# print(max(d))   # Output : TypeError: '<' not supported between instances of 'str' and 'int'
# print(sorted(d))  # TypeError: '<' not supported between instances of 'str' and 'int'

e = [4, 3, 6, 1]
print(min(e))
print(max(e))
print(sorted(e))
print(sorted(e, reverse=True))

# count
f = [1, 5, 4, 1, 3, 6, 7, 2, 5, 1, 5]
print(f.count(1))

# index
print(f.index(5))

# reverse

f.reverse()     # It is a permenent operation 
print(f)

# sort (vs sorted)  sort is a permenent operation while sorted is a temporary operation

g = [ 1, 4, 6, 2, 7, 0]
print(g)            #[1, 4, 6, 2, 7, 0]
print(sorted(g))    #[0, 1, 2, 4, 6, 7]
print(g)            #[1, 4, 6, 2, 7, 0]
g.sort()
print(g)            #[0, 1, 2, 4, 6, 7]
print()

# copy --> shallow copy

print(g)        #[0, 1, 2, 4, 6, 7]
print(id(g))    # 2313631463104
h = g.copy()
print(h)        # [0, 1, 2, 4, 6, 7]
print(id(h))    # 2313631463168

# List Comprehension
# List Comprehension provides a concise way of creating lists.
# newlist - [expression for item in iterable if condition == True]
# Advantages of List Comprehension
# 1. It is faster than using a for loop to create a list.
# 2. More time-efficient and space-efficient than loops.
# 3. Require fewer lines of Code
# 4. Transforms iterative statement into a formula.

# Add 1 to 10 numbers to a list

# i = []

# for a in range(1, 11):
#     i.append(a)
# print(i)

# Or

i = [a for a in range(1, 11)]
print(i)    # Output : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# scalar multiplication on a vector

j = [ 2, 3, 4]
s = 3
# print(j*3)      # Output : [2, 3, 4, 2, 3, 4, 2, 3, 4], but we wanted [6, 9, 12]

# x = []
# for i in j:
#     x.append(i*s)       # Output : [6, 9, 12]
    
# print(x)

# So we use list comprehension

print([s * i for i in j])   # Output : [6, 9, 12]

# Add squares
print([i**2 for i in j])    # Output : [4, 9, 16]

# Print all numbers divisible by 5 in the range of 1 to 50

print([i for i in range(1, 51) if i % 5 == 0])   # Output : 5 10 15 20 25 30 35 40 45

# Find languages which start with letter p
languages = ['java', 'python', 'php', 'c', 'javascript']
print([language for language in languages if language.startswith('p')]) #['python', 'php']

# Nested if with List Comprehension

basket = ['apple', 'guava', 'cherry', 'banana']
my_fruits = ['apple', 'kiwi', 'grapes', 'banana']
# add new list from my_fruits and items if the fruit exists in bsket and also starts with 'a

print([fruit for fruit in my_fruits if fruit in basket if fruit.startswith('a')])

# Print a (3, 3) matrix using list comprehension => nested list comprehension

print([[i*j for i in range(1, 4)] for j in range(1, 4)])    # Output : [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# Cartesian products -> List comprehension on 2 lists together
a1 = [1, 2, 3, 4]
a2 = [5, 6, 7, 8]

print([i*j for i in a1 for j in a2]) # Output : [5, 6, 7, 8, 10, 12, 14, 16, 15, 18, 21, 24, 20, 24, 28, 32]

# 2 ways to traverse a list
# itemwise and indexwise

# itemwise
for i in a1:
    print(i)
print()
    
# indexwise
for i in range(0, len(a1)):
    print(i)
    
    
#  Zip
# The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together.
# If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.

b1 = [1, 2, 3, 4]
b2 = [-1, -2, -3, -4]
print(zip(b1, b2))
print(list(zip(b1, b2)))
print([i+j for i, j in zip(b1, b2)]) # Output : [0, 0, 0, 0]

q = [1, 2, print, type, input]
print(q)    # Python can store any type of object

# Disadvantages of Python Lists
# 1. slow
# 2. memory intensive, eats up more memory
# 3. Risky usage because list are immutable