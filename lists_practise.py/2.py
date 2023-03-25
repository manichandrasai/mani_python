# Write a program to convert a list of characters into a single string.
# # Sample Input
#  ['a', 'b', 'c', 'd']
# # Expected Output
#  abcd
l = ['a','b','c','d']
m = ''.join(l)
print(m)
# method 2
for i in l:
    print(i,end = "" )