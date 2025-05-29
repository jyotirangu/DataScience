# Create 2 lists from a given list where 
# 1st list will contain all the odd numbers from the original list and
# the 2nd one will contain all the even numbers 

L = [1,2,3,4,5,6]

odd = []
even = []

for i in L:
  if i % 2 == 0:
    even.append(i)
  else:
    odd.append(i)

print("Even List ", even)
print("Odd List ", odd)

# USING LIST COMPREHENSION

L = [1,2,3,4,5,6]

even = [i for i in L if i % 2 == 0]
odd = [i for i in L if i % 2 != 0]

print(even)
print(odd)


# How to take list as input from user
# Input of fixed size
n = int(input('Enter the number of elements : '))

element=[]

for i in range(0, n):
  val = int(input("Enter the element : "))
  element.append(val)

print(element)


# Write a program to merge 2 list without using the + operator
L1 = [1,2,3,4]
L2 = [5,6,7,8]

merge_list = L1.copy()
merge_list.extend(L2)

print(merge_list)

# ORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR


L1 = [1,2,3,4]
L2 = [5,6,7,8]

merge_list = L1.copy()
for i in L2:
  merge_list.append(i)

print(merge_list)


# Write a program to replace an item with a different item if found in the list 
L = [1,2,3,4,5,3]
# replace 3 with 300

for i in range(len(L)):
  if L[i] == 3:
     L[i] = 300

print("Updated list : ", L)

# Write a program that can convert a 2D list to 1D list

L = [[1,2], [1,3], [1,4], [1,5]]
M = [item for sublist in L for item in sublist]
print(M)


# Write a program to remove duplicate items from a list

L = [1,2,1,2,3,4,5,3,4]
unique = []

for item in L:
  if item not in unique:
    unique.append(item)

print(unique)


L = [2,4,6,6,1,3,8]

if L == sorted(L):
  print("List is in ascending order")
else:
  print("List is not in ascending order")
