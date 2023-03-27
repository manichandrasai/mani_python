# Write a program to find difference between sum of even indexed and odd indexed numbers in a list of numbers. [Note:- Consider 0th index as even indexed]
# # Sample Input
#  list1 = [2, 4, 3, 9, 13, 12, 7, 6, 1, 5]
# # Expected Output
#  -10
l = [2, 4, 3, 9, 13, 12, 7, 6, 1, 5]
even_sum = 0
odd_sum = 0
for i in range (len(l)):
    if i % 2 == 0:
        even_sum += l[i]
    else:
        odd_sum += l[i]
diff = even_sum - odd_sum
print(diff)                       



