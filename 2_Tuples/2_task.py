# Q1: Join Tuples if similar initial element
# While working with Python tuples, we can have a problem in which we need to perform concatenation of records from the similarity of initial element. This problem can have applications in data domains such as Data Science.

# For eg.

# Input  : test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
# Output : [(5, 6, 7, 8), (6, 10), (7, 13)] 

test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 

unique = []

for i in test_list:
  unique.append(i[0])
unique = set(unique)

result = []

for i in unique:
  result.append([i])
  for j in test_list:
    if j[0] == i:
      result[-1].append(j[1])
print(list(map(tuple,result)))


# Q2: Multiply Adjacent elements (both side) and take sum of right and lest side multiplication result.
# For eg.

# The original tuple : (1, 5, 7, 8, 10)
# Resultant tuple after multiplication : 

# (1*5, 1*5+5*7, 7*5 + 7*8, 8*7 + 8*10, 10*8) -> (5, 40, 91, 136, 80)

# output-(5, 40, 91, 136, 80)

t = (1, 5, 7, 8, 10)

L = []

L.append(t[0]*t[1])

for i in range(1, len(t)-1):
  L.append(t[i]*t[i-1] + t[i]*t[i+1])

L.append(t[-1]*t[-2])

print(tuple(L))


# Q3: Check is tuples are same or not?
# Two tuples would be same if both tuples have same element at same index

# t1 = (1,2,3,0)
# t2 = (0,1,2,3)

# t1 and t2 are not same


t1 = (1,2,3,0)
t2 = (0,1,2,3)

flag = True
for i,j in list(zip(t1, t2)):
  if i == j:
    continue
  else:
    flag = False
    break

if flag:
  print("t1 and t2 are same")
else:
  print("t1 and t2 are not same")
  
  
# Q4: Count no of tuples, list and set from a list
# list1 = [{'hi', 'bye'},{'Geeks', 'forGeeks'},('a', 'b'),['hi', 'bye'],['a', 'b']]
# Output:

# List-2
# Set-2
# Tuples-1


L = [{'hi', 'bye'},{'Geeks', 'forGeeks'},('a', 'b'),['hi', 'bye'],['a', 'b']]

output = [0, 0, 0]

for i in L:
  if type(i) == list:
    output[0] += 1
  elif type(i) == set:
    output[1] += 1
  elif type(i) == tuple:
    output[2] += 1
  else:
    pass

print("List-{}\nSet-{}\nTuple-{}".format(output[0],output[1],output[2]))



# Q5: Shortlist Students for a Job role
# Ask user to input students record and store in tuples for each record. Then Ask user to input three things he wants in the candidate- Primary Skill, Higher Education, Year of Graduation.

# Show every students record in form of tuples if matches all required criteria.

# It is assumed that there will be only one primry skill.

# If no such candidate found, print No such candidate

# Input:

# Enter No of records- 2
# Enter Details of student-1
# Enter Student name- Manohar
# Enter Higher Education- B.Tech
# Enter Primary Skill- Python
# Enter Year of Graduation- 2022
# Enter Details of student-2
# Enter Student name- Ponian
# Enter Higher Education- B.Sc.
# Enter Primary Skill- C++
# Enter Year of Graduation- 2020

# Enter Job Role Requirement
# Enter Skill- Python
# Enter Higher Education- B.Tech
# Enter Year of Graduation- 2022
# Output

# ('Manohar', 'B.tech', 'Python', '2022')


students = []

num = int(input("Enter the number of applicants"))

for i in range(num):
  print("Enter details of ", i+1," applicant:")
  name = input("Enter name : ")
  h_ed = input("Enter higher education : ")
  p_skill = input("Enter Primary skill : ")
  yog = input("Enter year of graduation :")

  students.append((name,h_ed,p_skill,yog))
print(students)

required_skill = input("Enter required skill : ")
required_hed = input("Enter required higher education : ")
required_yog = input("Enter required year of graduation : ")
flag = False
for i in students:
  if i[2] == required_skill and i[1] == required_hed and i[3] == required_yog:
    print(i)
    flag = True

if flag == False:
  print("No matches found")