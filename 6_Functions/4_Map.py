# Map

# square the items of a list
list(map(lambda x:x**2,[1,2,3,4,5]))

# output : [1, 4, 9, 16, 25]

# odd/even labelling of list items
L = [1,2,3,4,5]
list(map(lambda x:'even' if x%2 == 0 else 'odd',L))

# Output : ['odd', 'even', 'odd', 'even', 'odd']

# fetch names from a list of dict

users = [
    {
        'name':'Rahul',
        'age':45,
        'gender':'male'
    },
    {
        'name':'Nitish',
        'age':33,
        'gender':'male'
    },
    {
        'name':'Ankita',
        'age':50,
        'gender':'female'
    }
]

list(map(lambda users:users['gender'],users))

# output : ['male', 'male', 'female']

