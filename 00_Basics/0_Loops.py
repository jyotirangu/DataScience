# While loop example -> program to print the table
# Program -> Sum of all digits of a given number
# Program -> keep accepting numbers from users till he/she enters a 0 and then find the avg

number = int(input('Enter the number'))
i = 1

while i<11:
    print(number,'*',i,'=',number * i)
    i += 1
 
   
#while loop with else

x = 1
while x < 3:
    print(x)
    x += 1

else:
    print('limit crossed')
    
    
#Guessing Game

# Generate a random integer between 1 and 100

import random
jackpot = random.randint(1,100)

guess = int(input('Guess'))
counter = 1
while guess != jackpot:
    if guess < jackpot:
        print("Wrong guess!! Guess higher")
    else:
        print('Wrong guess!! Guess lower')
    
    guess = int(input("Guess"))
    counter += 1
    
else:
    print("Correct guess")
    print("Attempts : ", counter)
    
    
# For loop Demo

for i in {1,2,3,4,5}:
    print(i)
    

# For Loop examples
#Program - The current population of a town is 10000. The population of the town is increasing at the rate of 10% per year. You have to write a program to find out the population at the end of each of the last 10 years.

cur_pop = 10000

for i in range(10,0,-1):
    print(i, cur_pop)
    cur_pop = cur_pop - 0.1 * cur_pop
    
    
# SEquence sum
# 1/1! + 2/2! + 3/3! + ...

n = int(input("Enter n :"))

result = 0
fact = 1

for i in range(1,n+1):
    fact = fact * i
    result = result + (i/fact)

print(result)

#Nested Loops
# Pattern 1
# *
# **
# ***

rows = int(input("Enter the number of rows : "))

for i in range(1, rows+1):
    for j in range(1, i+1):
        print("*", end="")
    print()
    
    
# Pattern 2
# 1
# 121
# 12321
# 1234321

rows = int(input("Enter the number of rows : "))

for i in range(1, rows+1):
    for j in range(1, i+1):
        print(j, end="")
    for k in range(i-1,0,-1):
        print(k, end="")
    print()
    
    
# Loop Control Statement

for i in range(1,10):
    if i == 5:
        break
    print(i)
    
lower = int(input('enter lower range'))
upper = int(input('enter upper range'))

for i in range(lower,upper+1):
  for j in range(2,i):
    if i%j == 0:
      break
  else:
    print(i)
    
# Continue
for i in range(1,10):
  if i == 5:
    continue
  print(i)
 
# Pass
for i in range(1,10):
  pass