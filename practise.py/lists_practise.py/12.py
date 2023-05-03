# Write a program to print the list of numbers which are greater than the average of numbers in the following list.
# # Sample Input
#  list1 = [2, 4, 3, 9, 13, 12, 7, 6, 1, 5]
# # Expected Output
#  [9, 13, 12, 7]
l = [2, 4, 3, 9, 13, 12, 7, 6, 1, 5]
avg = sum(l)/len(l)
m = []
for i in l:
    if(i > avg):
        m.append(i)
print(m)        