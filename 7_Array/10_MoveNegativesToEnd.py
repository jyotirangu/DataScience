l = [1, -2, 3, -4, 5, -6]
pos = []
neg = []

for i in l:
  if i < 0:
    neg.append(i)
    print("If - i = {} - {}".format(i,neg))
  else:
    pos.append(i)
    print("else - i = {} - {}".format(i,pos))

result = pos + neg

print(result)