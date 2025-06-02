# Benefits of using a Function
# Code Modularity
# Code Readibility
# Code Reusability
# Lambda Function
# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.



# x -> x^2
lambda x:x**2

# output : <function __main__.<lambda>(x)>

# x,y -> x+y
a = lambda x,y:x+y
a(5,2)

# output: 7


# Diff between lambda vs Normal Function
# No name
# lambda has no return value(infact,returns a function)
# lambda is written in 1 line
# not reusable
# Then why use lambda functions?
# They are used with HOF

# check if a string has 'a'
a = lambda s:'a' in s
a('hello')

# output : False 


# odd or even
a = lambda x:'even' if x%2 == 0 else 'odd'
a(6)

# output : 'even'