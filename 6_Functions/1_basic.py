# Let's create a function(with docstring)

def is_even(num):
    """
  This function returns if a given number is odd or even
  input - any valid integer
  output - odd/even
  created on - 2nd June 2025
    """
    if type(num) == int:
        if num % 2 == 0:
            return 'even'
        else:
            return 'odd'
    else:
        return 'pagal hai kya?'

# function
# function_name(input)
for i in range(1,11):
  x = is_even(i)
  print(x)
  
# 2 Point of views
is_even('hello')

# output : pagal hai kya?
  
  
print(is_even.__doc__)
print(type.__doc__)


# output:
#     This function returns if a given number is odd or even
#   input - any valid integer
#   output - odd/even
#   created on - 2nd June 2025
  
# type(object) -> the object's type
# type(name, bases, dict, **kwds) -> a new type


# Parameters Vs Arguments
# Types of Arguments
# Default Argument
# Positional Argument
# Keyword Argument

def power(a=1,b=1):
      return a**b
  
# output : 1
  
# positional argument
power(2,3)

# Output : 8


# *args and **kwargs
# *args and **kwargs are special Python keywords that are used to pass the variable length of arguments to a function


# *args
# allows us to pass a variable number of non-keyword arguments to a function.

def multiply(*kwargs):
  product = 1

  for i in kwargs:
    product = product * i

  print(kwargs)
  return product

multiply(1,2,3,4,5,6,7,8,9,10,12)

# output : (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12)
# 43545600


# **kwargs
# **kwargs allows us to pass any number of keyword arguments.
# Keyword arguments mean that they contain a key-value pair, like a Python dictionary.

def display(**salman):

  for (key,value) in salman.items():
    print(key,'->',value)
    
display(india='delhi',srilanka='colombo',nepal='kathmandu',pakistan='islamabad')

# output:
# india -> delhi
# srilanka -> colombo
# nepal -> kathmandu
# pakistan -> islamabad

# Points to remember while using *args and **kwargs
# order of the arguments matter(normal -> *args -> **kwargs)
# The words “args” and “kwargs” are only a convention, you can use any name of your choice


# Without return statement

L = [1,2,3]
print(L.append(4))
print(L)

# output :
#     None
# [1, 2, 3, 4]

# Variable Scope

def g(y):
    print(x)
    print(x+1)
x = 5
g(x)
print(x)

# Output :
#     5
#     6
#     5


def f(y):
    x = 1
    x += 1
    print(x)
x = 5
f(x)
print(x)

# OUtput :
#     2
#     5

# /////////////////////////////////////////////////////////////////
# def h(y):
#     x += 1 -----> error
# x = 5
# h(x)
# print(x)

# This will throw a error, beacuse in function you can use global variable but can not change it.

# ////////////////////////////////////////////////////////////////////


def f(x):
        x = x + 1
        print('in f(x): x =', x)
        return x

x = 3
z = f(x)
print('in main program scope: z =', z)
print('in main program scope: x =', x)

# output:
# in f(x): x = 4
# in main program scope: z = 4
# in main program scope: x = 3


# Nested Functions

def f():
    def g():
        print('inside function g')
        f()
    g()
    print('inside function f')
    
f()


# output : infinte loop 
# RecursionError: maximum recursion depth exceeded


def g(x):
    def h():
        x = 'abc'
    x = x + 1
    print('in g(x): x =', x)
    h()
    return x

x = 3
z = g(x)
print(z)

# output :
# in g(x): x = 4
# 4


def g(x):
    def h(x):
        x = x+1
        print("in h(x): x = ", x)
    x = x + 1
    print('in g(x): x = ', x)
    h(x)
    return x

x = 3
z = g(x)
print('in main program scope: x = ', x)
print('in main program scope: z = ', z)

# output:
# in g(x): x =  4
# in h(x): x =  5
# in main program scope: x =  3
# in main program scope: z =  4


# Functions are 1st class citizens

# type and id
def square(num):
  return num**2

type(square)

id(square)

# output:140471717004784

# reassign
x = square
id(x)
x(3)

# output : 9


# deleting a function
# del square

# output : NameError: name 'square' is not defined

# square(3)

# output : NameError: name 'square' is not defined

# storing
L = [1,2,3,4,square]
L[-1](3)

# output : 9

s = {square}
s

# output: {<function __main__.square(num)>}


# returning a function
def f():
    def x(a, b):
        return a+b
    return x
    
val = f()(3,4)
print(val)

# output : 7

# function as argument

def func_a():
    print('inside func_a')

def func_b(z):
    print('inside func_c')
    return z()

print(func_b(func_a))

# output:
# inside func_c
# inside func_a
# None


