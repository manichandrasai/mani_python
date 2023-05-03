# Write a Python program to find common items from two lists.
# # Sample Input
#  color1 = ["Red", "Green", "Orange", "White"]
#  color2 = ["Black", "Green", "White", "Pink"]
# # Expected Output
#  ['Green', 'White']
l = ["Red", "Green", "Orange", "White"]
m = ["Black", "Green", "White", "Pink"]
s = []
for i in l:
    if i in m:
        s.append(i)
print(s)