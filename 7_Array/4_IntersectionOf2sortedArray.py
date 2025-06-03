# Find intersection of 2 sorted arrays

a = [1,2,3,4,5,8]
b = [3,6,7,8]

for i in a:
  if i in b:
    print(i)
    
# n*2 due to in opertor

a = [1,2,3,4,5,8]
b = [3,6,7,8]
i = j = 0

while i<len(a) and j<len(b):
  if a[i]==b[j]:
    print(a[i])
    i += 1
    j += 1
  elif a[i] > b[j]:
    j+=1

  else:
    i+=1