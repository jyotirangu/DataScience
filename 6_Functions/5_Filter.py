# Filter

# numbers greater than 5
L = [3,4,5,6,7]

list(filter(lambda x:x>5,L))

# output : [6, 7]

# fetch fruits starting with 'a'
fruits = ['apple','guava','cherry']

list(filter(lambda x:x.startswith('a'),fruits))

# output : ['apple']