l = [1,0,0,1,1,0,1,0,0,1,1]

left = 0
right = len(l)-1

while left < right:
  if l[left] > l[right]:
    temp = l[left]
    l[left] = l[right]
    l[right] = temp

    left += 1
    right -= 1
    print("In while : ", l)

  elif l[left] == 0:
    left += 1

  elif l[right] == 1:
    right -= 1

print(l)