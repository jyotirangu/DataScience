# Rotate array to left d items

L = [1,2,3,4,5]
rotate = 2

for i in range(rotate):
  temp = L[0]
  for j in range(0,len(L)-1):
    L[j] = L[j+1]
  L[len(L)-1] = temp

print(L)