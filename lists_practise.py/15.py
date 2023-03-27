# Given a Python list, write a program to find the value 20 in the list, and if it is present, replace the first occurrence of a value with 200.
# # Sample Input
#  list1 = [5, 10, 15, 20, 25, 50, 20]
# # Expected Output
#  list1= [5, 10, 15, 200, 25, 50, 20]
l = [5, 10, 15, 20, 25, 50, 20]
if(20 in l):
    index = l.index(20)
    l[index] = 200
print(l)    
