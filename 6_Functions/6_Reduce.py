# Reduce

# sum of all item
import functools

functools.reduce(lambda x,y:x+y,[1,2,3,4,5])

# output : 15

# find min
functools.reduce(lambda x,y:x if x<y else y,[23,11,45,10,1])

# output: 1