# Find continous subarray with a given sum(given non-negative numbers)
# return the starting and ending index of the subarray
# return 1st subarray in case of multiple

L = [1,22,13,7,9,11,10]
S = 16

for i in range(0,len(L)):
  subarray = []
  for j in range(i,len(L)):
    subarray.append(L[j])
    if sum(subarray) == S:
      print(subarray)
      
# n*2


# Optimal code  


L = [1,22,13,7,9,11,10]

S = 35

d = {}
curr_sum = 0

for i in range(len(L)):
  curr_sum = curr_sum + L[i]

  if (curr_sum - S) in d:
    print(d[curr_sum - S]+1,i)
    break

  d[curr_sum] = i