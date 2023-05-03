# Write a Python program to remove duplicates from a list.
# # Sample Input
#  list1 = [10,20,30,20,10,50,60,40,80,50,40]
# # Expected Output
#  [10, 20, 30, 50, 60, 40, 80]
list1 = [10,20,30,20,10,50,60,40,80,50,40]
m = []
for i in list1:
    if i not in m:
        m.append(i)
print(m)        
