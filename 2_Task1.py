
# Problem 1: Write a program that will give you in hand monthly salary after deduction on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction as below:
# Salary(Lakhs) : Tax(%)

# Below 5 : 0%
# 5-10 : 10%
# 10-20 : 20%
# aboove 20 : 30%

salary = float(input("Enter the salary : "))
tax = 0
salary = salary*100000
HRA = salary * 0.1
DA = salary * 0.05
PF = salary * 0.03

if salary < 500000:
  tax = 0

elif salary >= 500000 and salary <1000000 :
  tax = salary * 0.1

elif salary >= 1000000 and salary <2000000 :
  tax = salary * 0.2

else:
  tax = salary * 0.3

in_hand_salary = salary - (HRA + DA + PF + tax)
print("In-hand salary:", in_hand_salary)


# Problem 2: Write a program that take a user input of three angles and will find out whether it can form a triangle or not.


a = int(input("Enter the angle 1 : "))
b = int(input("Enter the angle 2 : "))
c = int(input("Enter the angle 3 : "))

if a > 0 and b > 0 and c > 0:
  if (a+b+c) == 180:
    print("Triangle can be formed")
  else:
    print("Triangle can not be formed")

else:
  print("Triangle can not be formed")
  
  
# Problem 3: Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit.


cost_price = float(input("Enter the cost price : "))
selling_price = float(input("Enter the selling price : "))

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



while(True):
  print("1. cm to ft")
  print("2. km to miles")
  print("3. USD to INR")
  print("4. exit")

  choose = int(input("choose : "))

  if choose == 1:
    value = float(input("Enter the value : "))
    ft = value/30.48
    print("Value in feet: ", ft)

  elif choose == 2:
    value = float(input("Enter the vlaue : "))
    miles = value/1.609
    print("Value in miles: ", miles)
  
  elif choose == 3:
    value = float(input("Enter the vlaue : "))
    INR = value*85.17
    print("Value in INR : ", INR)

  elif choose == 4:
    break
  
  else:
    print("Invalid choice. Please try again.")
    
    
# Problem 5 - Exercise 12: Display Fibonacci series up to 10 terms.
# Note: The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it. The first two numbers are 0 and 1. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34


n0 = 0
n1 = 1
ans = 0
n = int(input("Enter the value : "))

print(n0,n1,end=" ")
for i in range(1, n-1):
  ans = n0+n1
  print(ans, end=" ")
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
flag = True
while(flag):
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



