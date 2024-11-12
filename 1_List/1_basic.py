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

git remote add origin https://github.com/jyotirangu/DataScience.git
git branch -M main
git push -u origin main