L = [1,2,3,4,5]

flag = True

for i in range(0,len(L)-1):
  if L[i] > L[i+1]:
    flag = False

if flag:
  print('sorted')
else:
  print('not sorted')