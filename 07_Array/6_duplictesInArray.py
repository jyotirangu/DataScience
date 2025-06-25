L = [1,1,2,3,4,4,5,5]
d={}
for i in L:
  if i in d:
    d[i] = d[i] + 1
  else:
    d[i] = 1
for i in d:
  if d[i] > 1:
    print(i)
    
    
# Find the first element to occur k times in an array

L = [1,1,2,3,4,4,5,5]

k = 2

d = {}

for i in L:
  if i in d:
    d[i] = d[i] + 1
  else:
    d[i] = 1

for i in d:
  if d[i] == k:
    print(i)
    break