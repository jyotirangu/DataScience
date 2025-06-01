# Q1: Write a program to find set of common elements in three lists using sets.
# Input : ar1 = [1, 5, 10, 20, 40, 80]
#         ar2 = [6, 7, 20, 80, 100]
#         ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

# Output : [80, 20]

ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

s1 = set(ar1)
s2 = set(ar2)
s3 = set(ar3)

print(list((s1&s2)&s3))


# Q2: Write a program to count unique number of vowels using sets in a given string. Lowercase and upercase vowels will be taken as different.
# Input:

# Str1 = "hands-on data science mentorship progrAm with live classes at affordable fee only on CampusX"
# Output:

# No of unique vowels-6

s = set("hands-on data science mentorship progrAm with live classes at affordable fee only on CampusX")
vowels = set('aeiouAEIOU')

print("No. of unique vowels-",len(s & vowels))


# Q3: Write a program to Check if a given string is binary string of or not.
# A string is said to be binary if it's consists of only two unique characters.

# Take string input from user.

# Input: str = "01010101010"
# Output: Yes

# Input: str = "1222211"
# Output: Yes

# Input: str = "Campusx"
# Output: No


s = "Campusx"

if len(set(s)) == 2:
  print("Yes, Binary")
else:
  print("No, not Binary")
  
  
# Q4: find union of n arrays.
# Example 1:

# Input:

# [[1, 2, 2, 4, 3, 6],
#  [5, 1, 3, 4],
#  [9, 5, 7, 1],
#  [2, 4, 1, 3]]
# Output:

# [1, 2, 3, 4, 5, 6, 7, 9]


L = [[1, 2, 2, 4, 3, 6],
 [5, 1, 3, 4],
 [9, 5, 7, 1],
 [2, 4, 1, 3]]

s = set()

for i in L:
  s.update(i)
print(s)


# Q5: Intersection of two lists. Intersection of two list means we need to take all those elements which are common to both of the initial lists and store them into another list. Only use using list-comprehension.

# Example 1:
# Input:
# lst1 = {15, 9, 10, 56, 23, 78, 5, 4, 9}
# lst2 = {9, 4, 5, 36, 47, 26, 10, 45, 87}

# Output:
# [9, 10, 4, 5]

# Example 2:
# Input:
# lst1 = {4, 9, 1, 17, 11, 26, 28, 54, 69}
# lst2 = {9, 9, 74, 21, 45, 11, 63, 28, 26}

# Output:
# [9, 11, 26, 28]


L1 = {15, 9, 10, 56, 23, 78, 5, 4, 9}
L2 = {9, 4, 5, 36, 47, 26, 10, 45, 87}

[i for i in L1 if i in L2]