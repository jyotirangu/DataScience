# Problem 1: Combine two lists index-wise(columns wise)
# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

# Given List:
# list1 = ["M", "na", "i", "Kh"]
# list2 = ["y", "me", "s", "an"]
# Output: [['M','y'], ['na', me'], ['i', 's'], ['Kh', 'an']]


list1 = ["M", "na", "i", "Kh"]
list2 = ["y", "me", "s", "an"]

[[i,j] for (i,j) in zip(list1, list2)]


# Problem 2: Add new item to list after a specified item
# Write a program to add item 7000 after 6000 in the following Python List

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# Output: [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]



list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)


# Problem 3: Update no of items available
# Suppose you are given a list of candy and another list of same size representing no of items of respective candy.

# i.e -
# candy_list = ['Jelly Belly','Kit Kat','Double Bubble','Milky Way','Three Musketeers']
# no_of_items = [10,20,34,74,32]
# Write a program to show no. of items of each candy type.
# Output:
# Jelly Belly-10
# Kit Kat-20
# Double Bubble-34
# Milky Way-74
# Three Musketeers-32



candy_list = ['Jelly Belly','Kit Kat','Double Bubble','Milky Way','Three Musketeers']
no_of_items = [10,20,34,74,32]

for (i,j) in zip(candy_list,no_of_items):
  print(i,"-",j)


# Problem 4: Running Sum on list
# Write a program to print a list after performing running sum on it.
# i.e:
# Input:
# list1 = [1,2,3,4,5,6]
# Output:[1,3,6,10,15,21]


list1 = [1,2,3,4,5,6]

new_list=[]
sum = 0

for i in list1:
  sum = sum + i
  new_list.append(sum)

print(new_list)


# Problem 5: You are given a list of integers. You are asked to make a list by running through elements of the list by adding all elements greater and itself.
# i.e. Say given list is [2,4,6,10,1] resultant list will be [22,20,10,23].

# For 1st element 2 ->> these are greater (4+6+10) values and 2 itself so on adding becomes 22.

# For 2nd element 4 ->> greater elements are (6, 10) and 4 itself, so on adding 20

# like wise for all other elememts.

# [2,4,6,10,1]-->[22,20,16,10,23]


list = [2,4,6,10,1]

result =[]
for i in list:
  sum = 0
  for j in list:
    if i<=j:
      sum += j

  result.append(sum)

print(result)


# Problem 6: Find list of common unique items from two list. and show in increasing order
# Input
# num1 = [23,45,67,78,89,34]
# num2 = [34,89,55,56,39,67]
# Output:[34, 67, 89]


num1 = [23,45,67,78,89,34]
num2 = [34,89,55,56,39,67]

result = []

for i in num1:
  if i in num2:
    if i not in result:
      result.append(i)

answer = sorted(result)
print(answer)


# Problem 7: Sort a list of alphanumeric strings based on product value of numeric character in it. If in any string there is no numeric character take it's product value as 1.
# Input:['1ac21', '23fg', '456', '098d','1','kls']
# Output:['456', '23fg', '1ac21', '1', 'kls', '098d']

L = ['1ac21', '23fg', '456', '098d','1','kls']
prod_value = []

for item in L:
  product = 1
  for char in item:
    if char.isdigit():
      product *= int(char)

  prod_value.append(product)
[i[1] for i in sorted(list(zip(prod_value,L)),reverse=True)]


# Problem 8: Split String of list on K character.
# Example :
# Input:['CampusX is a channel', 'for data-science', 'aspirants.']
# Output:['CampusX', 'is', 'a', 'channel', 'for', 'data-science', 'aspirants.']


L = ['CampusX is a channel', 'for data-science', 'aspirants.']
inp = ' '
res = []

for i in L:
  res.extend(i.split(inp))
  
print(res)


# Problem 9: Convert Character Matrix to single String using string comprehension.
# Example 1:
# Input:[['c', 'a', 'm', 'p', 'u', 'x'], ['i', 's'], ['b', 'e', 's', 't'], ['c', 'h', 'a', 'n', 'n', 'e', 'l']]
# Output:campux is best channel


list = [['c', 'a', 'm', 'p', 'u', 'x'], ['i', 's'], ['b', 'e', 's', 't'], ['c', 'h', 'a', 'n', 'n', 'e', 'l']]
print(" ".join(["".join(i) for i in L]))


# Problem 10: Add Space between Potential Words.
# Example:
# Input:['campusxIs', 'bestFor', 'dataScientist']
# Output:['campusx Is', 'best For', 'data Scientist']


test_list = ['campusxIs', 'bestFor', 'dataScientist']

res = []

for i in test_list:
  temp = [[]]
  for char in i:
    if char.isupper():
      temp.append([])

    temp[-1].append(char)

  temp_string = ""
  for item in temp:
    temp_string +="".join(item)+ " "
  res.append(temp_string[0:-1])

print(res)


# Problem 11: Write a program that can perform union operation on 2 lists
# Example:
# Input:
# [1,2,3,4,5,1]
# [2,3,5,7,8]
# Output:[1,2,3,4,5,7,8]


L1 = [1,2,3,4,5,1]
L2 = [2,3,5,7,8]

union = []

for i in L1:
  if i not in union:
    union.append(i)

for j in L2:
  if j not in union:
    union.append(j)

print(union)


# Problem 12: Write a program that can find the max number of each row of a matrix
# Example:
# Input:[[1,2,3],[4,5,6],[7,8,9]]
# Output:[3,6,9]


L = [[1,2,3],[4,5,6],[7,8,9]]

res =[]

for sublist in L:
  res.append(max(sublist))

print(res)


# Problem 13: Write a list comprehension to print the following matrix
# [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

[[j + 3*i for j in range(0,3)]for i in range(0,3)]


# Problem 14: Write a list comprehension that can transpose a given matrix
# matrix = [
# [1,2,3],
# [4,5,6],
# [7,8,9]
# ]

# [1, 4, 7]
# [2, 5, 8]
# [3, 6, 9]


matrix = [
[1,2,3],
[4,5,6],
[7,8,9]   
]

[[row[i] for row in matrix] for i in range(len(matrix))]


# Problem 15: Write a list comprehension that can flatten a nested list
# Input
# matrix = [
# [1,2,3],
# [4,5,6],
# [7,8,9]
# ]

# Output:[1, 2, 3, 4, 5, 6, 7, 8, 9]

matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]

[item for row in matrix for item in row]