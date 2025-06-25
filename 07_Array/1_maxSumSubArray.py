# Maximum sum subarray


L = [-2,4,7,-1,6,-11,14,3,-1,-6]

d = {}

for i in range(0,len(L)):
  subarray = []
  for j in range(i,len(L)):
    subarray.append(L[j])
    d[sum(subarray)] = subarray

max_val = max(d.keys())

for i in d:
  if i == max_val:
    print(d[i])
    
    
    
# Optimal code using Kadane's algo

L = [-2,4,7,-1,6,-11,14,3,-1,-6]


cur_sum = 0
cur_subarr = []
best_sum = L[0]
best_subarr = []


for i in L:
  if i + cur_sum > i:
    cur_sum = i + cur_sum
    cur_subarr.append(i)
  else:
    cur_subarr.clear()
    cur_subarr.append(i)
    cur_sum = i
  if cur_sum > best_sum:
      best_sum = cur_sum
      best_subarr = cur_subarr

print(best_subarr, best_sum)