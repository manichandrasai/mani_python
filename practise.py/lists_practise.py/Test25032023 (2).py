### 
# Test paper on List, Tuple and Dictionary in Python
###

"""
********* Count negative numbers *********

Write a program to return the number of negative numbers in the given list.
Sample Input: 
    [5, -1, -2, 0, 3]
Expected Output: 
    2

"""
a = [5, -1, -2, 0, 3]
n = 0
for i in a:
    if (i>n):
     n+=1
print(n)



# write your solution here for the above problem



"""
********* Gnereate Boolean List *********

Write a program to return a list with the same length as the given list L, where the value at index i is True if L[i] is greater than given number, and False otherwise.

Sample Input: 
    L = [1, 2, 3, 4], num = 2
Expected Output: 
    [False, False, True, True]
    
"""
l = [1,2,3,4]
num = 2
m = []
for i in l:
   if i>num:
      m.append(True)
   else:
      m.append(False)
print(m)

# write your solution here for the above problem



"""
********* Remove all elements having duplicates *********

Write a program to print a list of all elements in a list that have only a single occurrence. 

For example, if the contents of the list is 
    [7, 5, 5, 1, 6, 7, 8, 7, 6], 
it should return 
    [1, 8]

"""
l = [7, 5, 5, 1, 6, 7, 8, 7, 6]
m = []
for i in l:
   if l.count(i) == 1:
      m.append(i)
print(m)


# write your solution here for the above problem



"""
********* Helping with the Budget *********

John has a hard time keeping his budget. Write a program to help him analyze his spendings. 
You are given a list with John's spendings for each month. Go through the list, and count the number of times...
    a. the spendings were low (< 1000.0)
    b. the spendings were normal (between 1000.0 and 2500.0 inclusive)
    c. the spendings were high (> 2500.0)
Then, print the following to the output:
    Numbers of months with low spendings: {}, normal spendings: {}, high spendings: {}.

Let spendings = [1346.0, 987.50, 1734.40, 2567.0, 3271.45, 2500.0, 2130.0, 2510.30, 2987.34, 3120.50, 4069.78, 1000.0]

"""
l = [1346.0, 987.50, 1734.40, 2567.0, 3271.45, 2500.0, 2130.0, 2510.30, 2987.34, 3120.50, 4069.78, 1000.0]

low_count = 0
normal_count = 0
high_count = 0

for spending in l:
    if (spending < 1000.0):
        low_count += 1
    elif( 1000.0 <= spending <= 2500.0):
        normal_count += 1
    else:
        high_count += 1

print("Numbers of months with low spendings: {}, normal spendings: {}, high spendings: {}.".format(low_count, normal_count, high_count))
# write your solution here for the above problem


"""
********* All Roads Lead to Rome ********* 

You are given a list with various flight connections in Europe. Each connection is represented as a tuple with the following elements:
    (city_from, city_to, time)
For example, the following tuple represents a flight from Amsterdam to Dublin which takes 100 minutes:
    ('Amsterdam', 'Dublin', 100)

Your task is to go through all the routes in a loop and check how many of them lead to Rome (i.e. how many of them have city_to equal to 'Rome'). 
Among the routes to Rome, you should also calculate the average flight time. Print the following to the output:
    `{} connections lead to Rome with an average flight time of {} minutes`
Here you need to replace {} with "the number of connections" and "the average flight time".

Let connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170),
    ]
    
"""
l = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170),
    ]
c = 0
m = []
for i in l:
   if(i[1] == 'Rome'):
      c += 1
      m.append(i[2])
sum = 0
for i in m:
   sum += i
# print(sum)
average = sum//len(m)
# print(average)

print(f"the no of connections to rome is {c}, the average flight time to rome is {average}  min")   

      
        
        

# write your solution here for the above problem


"""
A company allows its employees to work in a hybrid model. Here given a dictionary of employee's work status on a day as input,
    statuses = {"Alice": "online", 
                "Bob": "offline", 
                "Eve": "online", 
                "Ravi": "online", 
                "sneha": "offline", 
                "vinod": "online", 
                "dheepika": "online"}
Write a program that should return the number of people who are online and Print the following to the output:
    `{} employees are working online`
Here you need to replace {} with "the number of employees who are online"

"""
statuses = {"Alice": "online", 
                "Bob": "offline", 
                "Eve": "online", 
                "Ravi": "online", 
                "sneha": "offline", 
                "vinod": "online", 
                "dheepika": "online"}
online = 0
for i in statuses.values():
   if i == "online":
      online += 1
print(f"{online} employess are working online")      
print(f"the number of employes who are in online : {online}")      

# write your solution here for the above problem


"""
Write a program that reads a string from the user and create a dictionary having a key as word length and the value is the count of words of that length. 
For example, if the user enters 
    'A fat cat is on the mat'
    
        Word    Word length
        A       1
        fat     3
        cat     3
        is      2
        on      2
        the     3
        mat     3

The print the following to the output: 
    {1:1, 3:4, 2:2}
In the output, keys are word lengths and values are their count.

"""

# write your solution here for the above problem
from collections import Counter
res = {}
sen  =  'A fat cat is on the mat'
data = sen.split()
for x in data:
   res[x] = len(x)
# print(res)   
res =res.values()
c = dict(Counter(res))
print(c)