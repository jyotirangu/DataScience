
# Strings are sequence of Characters

# In Python specifically, strings are a sequence of Unicode Characters

# Creating Strings
# Accessing Strings
# Adding Chars to Strings
# Editing Strings
# Deleting Strings
# Operations on Strings
# String Functions

# Creating Stings

s = 'hello'
s = "hello"
# multiline strings
s = '''hello'''
s = """hello"""
s = str('hello')
print(s)


# Accessing Substrings from a String
# Positive Indexing
s = 'hello world'
print(s[4])

# Negative Indexing
s = 'hello world'
print(s[-3])


# Slicing
s = 'hello world'
print(s[6:0:-2]) #wol
print(s[::-1]) #dlrow olleh
print(s[-1:-6:-1]) #dlrow


# Editing and Deleting in Strings


# s = 'hello world'
# s[0] = 'H'

# # Python strings are immutable

# s = 'hello world'
# del s
# print(s)
# NameError: name 's' is not defined


# Operations on Strings
# Arithmetic Operations
# Relational Operations
# Logical Operations
# Loops on Strings
# Membership Operations

print('delhi' + ' ' + 'mumbai')
# delhi mumbai

print('delhi'*5)
# delhidelhidelhidelhidelhi

print("*"*50)
# **************************************************

'delhi' != 'delhi'
# False

'mumbai' > 'pune'
# lexiographically
# False

'Pune' > 'pune'
# False

'hello' and 'world'
# world

'hello' or 'world'
# hello

'' and 'world'
# ''

'' or 'world'
# world

'hello' or 'world'
# hello

'hello' and 'world'
# world

not 'hello'
# False

'D' in 'delhi'
# False



# Common Functions
# len
# max
# min
# sorted

len('hello world')
# 11

max('hello world')
# w

min('hello world')
# ' '

sorted('hello world',reverse=True)
# ['w', 'r', 'o', 'o', 'l', 'l', 'l', 'h', 'e', 'd', ' ']

# Capitalize/Title/Upper/Lower/Swapcase

s = 'hello world'
print(s.capitalize())
print(s)

# Hello world
# hello world

s.title()
# Hello World

s.upper()
# HELLO WORLD

'Hello Wolrd'.lower()
# hello wolrd

'HeLlO WorLD'.swapcase()
# hElLo wORld

# Count/Find/Index

'my name is nitish'.count('i')
# 3

'my name is nitish'.find('x')
# -1

# 'my name is nitish'.index('x')
# ValueError: substring not found

# endswith/startswith

'my name is nitish'.endswith('sho')
# False

'my name is nitish'.startswith('1my')
# False

# format

name = 'nitish'
gender = 'male'

'Hi my name is {1} and I am a {0}'.format(gender,name)
# Hi my name is nitish and I am a male

# isalnum/ isalpha/ isdigit/ isidentifier
'nitish1234%'.isalnum()
# False

'nitish'.isalpha()
# True

'123abc'.isdigit()
# False 

'first-name'.isidentifier()
# False

# Split/Join

'hi my name is nitish'.split()
# ['hi', 'my', 'name', 'is', 'nitish']

'hi my name is nitish'.split('is')
# ['hi my name ', ' nit', 'h']

" ".join(['hi', 'my', 'name', 'is', 'nitish'])
# hi my name is nitish

# Replace

'hi my name is nitish'.replace('nitish','campusx')
# hi my name is campusx

# Strip
'nitish                           '.strip()
# nitish

# Example Programs


# Find the length of a given string without using the len() function

s = input('enter the string')

counter = 0

for i in s:
  counter += 1

print('length of string is',counter)


# Extract username from a given email. 
# Eg if the email is nitish24singh@gmail.com 
# then the username should be nitish24singh

s = input('enter the email')

pos = s.index('@')
print(s[0:pos])

# Count the frequency of a particular character in a provided string. 
# Eg 'hello how are you' is the string, the frequency of h in this string is 2.

s = input('enter the email: ')
term = input('what would like to search for: ')

counter = 0
for i in s:
  if i == term:
    counter += 1

print('frequency',counter)

# Write a program which can remove a particular character from a string.
s = input('enter the string')
term = input('what would like to remove')

result = ''

for i in s:
  if i != term:
    result = result + i

print(result)

# Write a program that can check whether a given string is palindrome or not.
# abba
# malayalam

s = input('enter the string')
flag = True
for i in range(0,len(s)//2):
  if s[i] != s[len(s) - i -1]:
    flag = False
    print('Not a Palindrome')
    break

if flag:
  print('Palindrome')

# Write a program to count the number of words in a string without split()

s = input('enter the string')
L = []
temp = ''
for i in s:

  if i != ' ':
    temp = temp + i
  else:
    L.append(temp)
    temp = ''

L.append(temp)
print(L)

# Write a python program to convert a string to title case without using the title()
s = input('enter the string')

L = []
for i in s.split():
  L.append(i[0].upper() + i[1:].lower())

print(" ".join(L))

# Write a program that can convert an integer to string.

number = int(input('enter the number'))

digits = '0123456789'
result = ''
while number != 0:
  result = digits[number % 10] + result
  number = number//10

print(result)
print(type(result))