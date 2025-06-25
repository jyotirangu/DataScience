# Problem 1 - Print the following pattern. Write a program to use for loop to print the following reverse number pattern.
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1

row = int(input("Enter the number of rows : "))
for i in range(1, row + 1):
  for j in range(row + 1 - i,0,-1 ):
    print(j, end=" ")
  print()
  
  
# Problem 2: Print the following pattern.
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

row = int(input("Enter the number of rows : "))

for i in range(1, row+1):
  for j in range(0, i):
    print("*", end=" ")
  print()

for i in range(1, row):
  for j in range(row-i, 0, -1):
    print("*", end=" ")
  print()
  
 
# Problem 3:Write a program to pring the following pattern
#     *
#   * * *
# * * * * * 


row = int(input("Enter the number of rows: "))

for i in range(1, row+1):
  for space in range(0, row+1-i):
    print(" ", end=" ")
  for star in range(0,i):
    print("*", end=" ")
  for star2 in range(1,i):
    print("*", end=" ")
  print()
  

# Problem 4:Write a program to print the following pattern
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

row = int(input("Enter the number of rows: "))

for i in range(1, row+1):
  for j in range(i, 0,-1):
    print(j, end=" ")
  print()
  

# Problem 5: Write a Python Program to Find the Sum of the Series till the nth term:
# 1 + x^2/2 + x^3/3 + … x^n/n
# n will be provided by the user

x = int(input("Enter the number of x : "))
n = int(input("Enter the number of n : "))

sum=1
s=''
print('1 + ', end='')
for i in range(2, n+1):
  sum = sum + x**i/i
  s = s + 'x^{}/{} + '.format(i,i)
print(s[:-2])
print(sum)


# Problem 7 - Find the sum of the series upto n terms.
# Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690. Take the user input and then calculate. And the output style should match which is given in the example.

# Example 1:
# Input:
# 5
# Output:
# 2+22+222+2222+22222
# Sum of above series is: 24690


n = int(input("Enter the number of terms : "))

start = 2
sum = 0

for i in range(0, n):
  if i < n-1:
    print(start, end = '+')
  else:
    print(start)

  sum = sum + start
  start = start*10 + 2

print(sum)

# Problem 8: Write a program to print all the unique combinations of 1,2,3 and 4
# Output:

# 1 2 3 4
# 1 2 4 3
# 1 3 2 4
# 1 3 4 2
# 1 4 2 3
# 1 4 3 2
# 2 1 3 4
# 2 1 4 3
# 2 3 1 4
# 2 3 4 1
# 2 4 1 3
# .
# .
# and so on


for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            for l in range(1,5):
                print(i, j, k, l)
                

# Problem 9: Write a program that will take a decimal number as input and prints out the binary equivalent of the number

n = int(input("Enter the number : "))
binary=[]
while n>0:

  binary.append(n%2)
  n = n//2
  print(n, binary)

for i in binary[::-1]:
  print(i, end='')
  
  
# Problem 10: Write a program that will take 2 numbers as input and prints the LCM and HCF of those 2 numbers


x = int(input("Enter 1st number : "))
y = int(input("Enter 2nd number : "))

if x>y:
  greater = x
  smaller = y
else:
  greater = y
  smaller = x

while True:
  if(greater % x == 0) and (greater % y == 0):
    lcm = greater
    break

  greater = greater + 1

for i in range(1, smaller+1):
  if(x % smaller == 0) and (y % smaller == 0):
    hcf = smaller


print(lcm)
print(hcf)


# Problem 11: Create Short Form from initial character
# Given a string create short form ofthe string from Initial character. Short form should be capitalised.

# Example:
# Input:Data science mentorship program
# Output:DSMP


inp = 'Data science memtorship program'

res=''

for i in inp.split():
  res = res + i[0].upper()

print(res)


# Problem 12: Append second string in the middle of first string
# Input:
# campusx
# data
# Output:camdatapusx


s1 = input('Enter the first string : ')
s2 = input('Enter the second string : ')

print(s1[0:int(len(s1)/2)] + s2 + s1[int(len(s1)/2):])


# Problem 13:Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.
# Given:
# str1 = PyNaTive
# Expected Output:yaivePNT


s = input('Enter the string : ')

lower = ''
upper = ''

for i in s:
  if i.islower():
    lower += i
  else: 
    upper += i
print(lower+upper)


# Problem 14:Take a alphanumeric string input and print the sum and average of the digits that appear in the string, ignoring all other characters.
# Input:hel123O4every093
# Output:
# Sum: 22
# Avg: 2.75


s = input('Enter the string : ')
counter = 0
sum = 0

for i in s:
  if i.isdigit():
    counter += 1
    sum += int(i)

print("Sum : ",sum)
print("Avg : ",sum/counter)


# Problem 15: Removal of all characters from a string except integers
# Given:
# str1 = 'I am 25 years and 10 months old'
# Expected Output:2510

s = 'I am 25 years and 10 months old'

res = ''

for i in s:
  if i.isdigit():
    res += i

print(res)


# Problem 16: Check whether the string is Symmetrical.
# Statement: Given a string. the task is to check if the string is symmetrical or not. A string is said to be symmetrical if both the halves of the string are the same.

# Example 1:

# Input:khokho
# Output:The entered string is symmetrical


s = input('Enter the string : ')

if len(s)%2 == 0:
  s1 = s[0:int(len(s)/2)]
  s2 = s[int(len(s)/2):]
else:
  s1 = s[0:int(len(s)//2)]
  s2 = s[int(len(s)//2) + 1 :]

if s1 == s2:
  print("Symmetrical")
else:
  print("Not Symmetrical")
  
  
# Problem 17: Reverse words in a given String
# Statement: We are given a string and we need to reverse words of a given string.

# Example 1:
# Input:geeks quiz practice code
# Output:code practice quiz geeks
# Example 2:
# Input:my name is laxmi
# Output:laxmi is name my


s = input('Enter the string :')

L=[]

for i in s.split():
  L.append(i)

L = L[::-1]

print(" ".join(L))



# Problem 18: Find uncommon words from two Strings.
# Statement: Given two sentences as strings A and B. The task is to return a list of all uncommon words. A word is uncommon if it appears exactly once in any one of the sentences, and does not appear in the other sentence. Note: A sentence is a string of space-separated words. Each word consists only of lowercase letters.

# Example 1:
# Input:
# A = "apple banana mango" 
# B = "banana fruits mango"
# Output:['apple', 'fruits']


A = "apple banana mango" 
B = "banana fruits mango"

L =[]

for i in A.split():
  if i not in B and i not in L:
    L.append(i)

for j in B.split():
  if j not in A and j not in L:
    L.append(j)

print(L)


# Problem 19: Word location in String.
# Statement: Find a location of a word in a given sentence.

# Example 1:
# Input:
# Sentence: We can learn data science through campusx mentorship program.
# word: campusx
# Output:Location of the word is 7.
# Note- Don't use index/find functions


s= "We can learn data science through campusx mentorship program."
word = "campusx"
pos = 0

for i in s.split():
  pos += 1
  if i == word:
    break

print("Location of the word is {}".format(pos))


# Problem 20: Write a program that can remove all the duplicate characters from a string. User will provide the input.

s = input('Enter the string :')
ans = ''
for i in s:
  if i not in ans:
    ans = ans + i
print(ans)