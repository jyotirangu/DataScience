# Find element with left side smaller/right side greater in an array

L = [3,1,2,5,8,7,9]

for i in range(1, len(L)-1):
  flag = True

  for j in range(0,i):
    if L[j] > L[i]:
      flag = False

  for k in range(i+1, len(L)):
    if L[k] < L[i]:
      flag = False

  if flag:
    print(L[i])

    # n*2
    
    
L = [3,1,2,5,8,7,9]

for i in range(1, len(L)-1):
  if max(L[:i]) < L[i] < min(L[i+1:]):
    print(L[i])

    # n*2 use of in_built function
    
    
L = [3,1,2,5,8,7,9]

max_arr = []
min_arr= []

max_val = L[0]
min_val = L[-1]

for i in L:
  if max_val < i:
    max_val = i
  max_arr.append(max_val)

for i in range(len(L)-1,-1,-1):
  if min_val >= L[i]:
    min_val = L[i]
  min_arr.insert(0,min_val)

for i in range(1, len(L)-1):
  if max_arr[i-1] < L[i] < min_arr[i+1]:
    print(L[i])

print(max_arr)
print(min_arr)

# n
