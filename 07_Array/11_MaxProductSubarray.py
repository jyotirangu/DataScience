l = [2, 3, -2, 4]


max_product = l[0]
current_max = l[0]
current_min = l[0]

for i in l[1:]:
  current_max = max(i,i * current_max)
  current_min = min(i,i * current_min)

  max_product = max(max_product, current_max)
print(max_product)