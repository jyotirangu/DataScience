
# Problem 1: Write a program that will give you in hand monthly salary after deduction on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction as below:
# Salary(Lakhs) : Tax(%)

# Below 5 : 0%
# 5-10 : 10%
# 10-20 : 20%
# aboove 20 : 30%

ctc = int(input("Enter the salary : "))

if ctc < 500000:
  salary = ctc*.82

elif ctc < 1000000:
  salary = ctc*.72

elif ctc<2000000 :
  salary = ctc*.62

else:
  salary = ctc*.52

print("Your in hand monthly salary will be:", round(salary/12.2))


# Problem 2: Write a program that take a user input of three angles and will find out whether it can form a triangle or not.


a = int(input("Enter the angle 1 : "))
b = int(input("Enter the angle 2 : "))
c = int(input("Enter the angle 3 : "))

if (a+b+c) == 180 and a > 0 and b > 0 and c > 0:
  print("Triangle can be formed")
else:
  print("Triangle can not be formed")
  
  
# Problem 3: Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit.


cost_price = int(input("Enter the cost price : "))
selling_price = int(input("Enter the selling price : "))

if cost_price > selling_price:
  print("Loss")

elif cost_price == selling_price:
  print("No profit, No loss")
  
else:
  print("Profit")
  
  
# Problem 4: Write a menu-driven program -
# cm to ft
# km to miles
# USD to INR
# exit



menu = input("""
  hi select an option
  1. cm to ft
  2. km to miles
  3. USD to INR
  4. exit
  
  """)

if menu == '1':
    cm = float(input("Enter the cm value : "))
    print("Value in feet: ", cm*0.032)

elif menu == '2':
    km = float(input("Enter the km vlaue : "))
    print("Value in miles: ", km*0.62)
  
elif menu == '3':
    usd = float(input("Enter the usdvlaue : "))
    print("Value in INR : ", usd*80.)
  
else:
    exit()
    
    
# Problem 5 - Exercise 12: Display Fibonacci series up to 10 terms.
# Note: The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it. The first two numbers are 0 and 1. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34


n0 = 0
n1 = 1
n = int(input("Enter the value : "))

for i in range(1, n+1):
  print(n0, end=" ")
  ans = n0+n1
  
  n0=n1
  n1=ans
  
print()
  
  
# Problem 6 - Find the factorial of a given number.
# Write a program to use the loop to find the factorial of a given number.


number = int(input("Enter the value : "))
fact = 1
for i in range(1, number+1):
  fact = fact*i

print(fact)


# Problem 7 - Reverse a given integer number.


num = int(input("Enter the number: "))
rev = 0

while num > 0:
  rev = (rev * 10) + (num % 10)
  num = num // 10

print(rev)


# Problem 8: Take a user input as integer N. Find out the sum from 1 to N. If any number if divisible by 5, then skip that number. And if the sum is greater than 300, don't need to calculate the sum further more. Print the final result. And don't use for loop to solve this problem.


num = int(input("Enter the value : "))
sum = 0
i = 1
while i <= num :
  if i%5 == 0:
    i += 1
    continue

  else:
      sum += i
      if sum > 300:
        sum -= i
        break

      i += 1


print(sum)


# Problem 9: Write a program that keeps on accepting a number from the user until the user enters Zero. Display the sum and average of all the numbers.


count = 0
sum = 0

while True:
  value = int(input("Enter the value : "))
  if value == 0:
    break

  count += 1
  sum += value
if count > 0:
  print("Sum: ", sum)
  sum /= count
  print("Average: ", sum)

else:
  print("NO numbers were entered")
  
  
# Problem 9: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.


result = []
for i in range(2000, 3201):
      if i % 7 == 0 and i % 5 != 0:
        result.append(str(i))
print(','.join(result))


# Problem 10: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number. The numbers obtained should be printed in a space-separated sequence on a single line.


L = []
for i in range(1000, 3001):
  flag = True

  current = i

  while current > 0:
    last = current%10
    if last%2 != 0:
      flag = False
      break
    current = current//10

  if flag:
    L.append(str(i))

print(", ".join(L))



# Problem 11: A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
# The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# !

# The numbers after the direction are steps.

# ! means robot stop there.

# Please write a program to compute the distance from current position after a sequence of movement and original point.

# If the distance is a float, then just print the nearest integer.

# Example:
# Input:

# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# !
# Output:

# 2


pos = [0,0]
while True:
  s = input('Enter the robot path ')
  if s=='!':
    break

  direction = s.split()[0]
  steps = int(s.split()[1])

  if direction == 'UP':
    pos[1] = pos[1] + steps
  elif direction == 'DOWN':
    pos[1] = pos[1] - steps
  elif direction == 'LEFT':
    pos[0] = pos[0] - steps
  elif direction == 'RIGHT':
    pos[0] = pos[0] + steps
  else:
    pass

print(int(round((pos[0]**2 + pos[1]**2)**0.5)))



# Problem 12:Write a program to print whether a given number is a prime number or not


num = int(input('Enter the num : '))

flag = True
for i in range(2, num):
  if num%i == 0:
    flag = False
    break

if flag:
  print('Prime')
else:
  print('Not Prime')
  
  
# Problem 13:Print all the Armstrong numbers in a given range.
# Range will be provided by the user
# Armstrong number is a number that is equal to the sum of cubes of its digits. For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.


start = int(input("Enter the start range : "))
end = int (input("Enter the end range: "))

for i in range(start, end):
    num = 0
    real=i
    
    while real > 0:
      num += ((real%10)**3)
      real = real//10
      
    if i==num:
          print(num, end=" ")
      


# Problem 14:Calculate the angle between the hour hand and minute hand.
# Note: There can be two angles between hands; we need to print a minimum of two. Also, we need to print the floor of the final result angle. For example, if the final angle is 10.61, we need to print 10.

# Input:
# H = 9 , M = 0
# Output:
# 90
# Explanation:
# The minimum angle between hour and minute hand when the time is 9 is 90 degress.
