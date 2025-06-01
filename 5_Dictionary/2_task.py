# Q1: Key with maximum unique values
# Given a dictionary with values list, extract key whose value has most unique values.

# Example 1:
# Input:test_dict = {"CampusX" : [5, 7, 9, 4, 0], "is" : [6, 7, 4, 3, 3], "Best" : [9, 9, 6, 5, 5]}
# Output:CampusX

# Example 2:
# Input:test_dict = {"CampusX" : [5, 7, 7, 7, 7], "is" : [6, 7, 7, 7], "Best" : [9, 9, 6, 5, 5]}
# Output:Best

test_dict = {"CampusX" : [5, 7, 9, 4, 0], "is" : [6, 7, 4, 3, 3], "Best" : [9, 9, 6, 5, 5]}

max_val = 0
max_key = ''

for i in test_dict:
  if max_val < len(set(test_dict[i])):
    max_val = len(set(test_dict[i]))
    max_key = i

print(max_key)


# Q2: Replace words from Dictionary. Given String, replace it’s words from lookup dictionary.

# Example 1:

# Input:
# test_str = 'CampusX best for DS students.'
# repl_dict = {"best" : "is the best channel", "DS" : "Data-Science"}
# Output:CampusX is the best channel for Data-Science students.

# Example 2:
# Input:
# test_str = 'CampusX best for DS students.'
# repl_dict = {"good" : "is the best channel", "ds" : "Data-Science"}
# Output:CampusX best for DS students.


test_str = 'CampusX best for DS students.'
repl_dict = {"best" : "is the best channel", "DS" : "Data-Science"}

result = []
for i in test_str.split():
  if i in repl_dict:
    result.append(repl_dict[i])
  else:
    result.append(i)

print(' '.join(result))


# Q3: Convert List to List of dictionaries. Given list values and keys list, convert these values to key value pairs in form of list of dictionaries.

# Example 1:
# Input:
# test_list = ["DataScience", 3, "is", 8]
# key_list = ["name", "id"]
# Output:[{'name': 'DataScience', 'id': 3}, {'name': 'is', 'id': 8}]

# Example 2:
# Input:
# test_list = ["CampusX", 10]
# key_list = ["name", "id"]
# Output:[{'name': 'CampusX', 'id': 10}]

test_list = ["DataScience", 3, "is", 8]
key_list = ["name", "id"]

n = len(test_list)

res = []

for i in range(0,n,2):
  res.append({key_list[0]: test_list[i],key_list[1]:test_list[i+1]})

print(res)


# Q4: Convert a list of Tuples into Dictionary.

# Example 1:Input:[("akash", 10), ("gaurav", 12), ("anand", 14), ("suraj", 20), ("akhil", 25), ("ashish", 30)]
# Output:{'akash': [10], 'gaurav': [12], 'anand': [14], 'suraj': [20], 'akhil': [25], 'ashish': [30]}

# Example 2:
# Input:[('A', 1), ('B', 2), ('C', 3)]
# Output:{'A': [1], 'B': [2], 'C': [3]}

L = [("akash", 10), ("gaurav", 12), ("anand", 14), ("suraj", 20), ("akhil", 25), ("ashish", 30)]

d = {}

for i,j in L:
  d[i] = [j]

print(d)


# Q5: Sort Dictionary key and values List.

# Example 1:
# Input:{'c': [3], 'b': [12, 10], 'a': [19, 4]}
# Output:{'a': [4, 19], 'b': [10, 12], 'c': [3]}

# Example 2:
# Input:{'c': [10, 34, 3]}
# Output:{'c': [3, 10, 34]}

d = {'c': [3], 'b': [12, 10], 'a': [19, 4]}

res = {}

for i in sorted(d):
  res[i] = sorted(d[i])

print(res)