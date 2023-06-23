# -----------------Practice Exercise--------
# Write a program that uses list and range to create the list [3,6, 9, . . . , 99] .
my_list = []
for num in range(3, 100, 3):
    my_list.append(num)

print(my_list)

# Write a program to convert a list of characters into a single string.

# # Sample Input
#  ['a', 'b', 'c', 'd']
# # Expected Output
#  abcd
char_list = ['a', 'b', 'c', 'd']
string = ''.join(char_list)
print(string)

# Write a program to read a string from the user and print the list of characters in the string.
# # Sample Input
#  abcd
# # Expected Output
#  ['a', 'b', 'c', 'd']
string = input("Enter a string: ")
char_list = list(string)
print(char_list)

# Write a Python program to find common items from two lists.
# # Sample Input
#  color1 = ["Red", "Green", "Orange", "White"]
#  color2 = ["Black", "Green", "White", "Pink"]
# # Expected Output
#  ['Green', 'White']
color1 = ["Red", "Green", "Orange", "White"]
color2 = ["Black", "Green", "White", "Pink"]
common_items = []
for item in color1:
    if item in color2:
        common_items.append(item)
print(common_items)

# Write a Python program to get the difference between the two lists.
# # Sample Input
#  list1 = [1, 2, 3, 4]
#  list2 = [1, 2]
# # Expected Output
#  [3,4]
list1 = [1, 2, 3, 4]
list2 = [1, 2]
difference = []
for item in list1:
    if item not in list2:
        difference.append(item)
print(difference)

# Write a Python program to get the largest number from a list.
# # Sample Input
#  list1 = [1, 2, -8, 0]
# # Expected Output
#  2
list1 = [1, 2, -8, 0]
list1.sort()
largest_number = list1[-1]
print(largest_number)

#    --------or--------

list1 = [1, 2, -8, 0]
largest_number = list1[0]
for num in list1:
    if num > largest_number:
        largest_number = num

print(largest_number)


# Write a Python program to find the second smallest number in a list.
# # Sample Input
#  list1 = [1, 2, -8, -2, 0]
# # Expected Output
#  -2
list1 = [1, 2, -8, -2, 0]
list1.sort()
second_smallest = list1[-1]
print(second_smallest)

# Write a Python program to remove duplicates from a list.
# # Sample Input
#  list1 = [10,20,30,20,10,50,60,40,80,50,40]
# # Expected Output
#  [10, 20, 30, 50, 60, 40, 80]
list = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
list1 = []
for num in list1:
    if num not in list1:
        list1.append(num)
print(list1)

# Write a Python program to sum all the items in a list.
# # Sample Input
#  list1 = [1, 2, -8]
# # Expected Output
#  -5
list1 = [1, 2, -8]
sum_of_items = 0
for num in list1:
    sum_of_items += num
print(sum_of_items)

# Write a Python program to multiply all the items in a list.
# # Sample Input
#  list1 = [1, 2, 3, 4]
# # Expected Output
#  24
list1 = [1, 2, 3, 4]
product_of_items = 1
for num in list1:
    product_of_items *= num
print(product_of_items)

# Write a program to find difference between sum of even indexed and odd indexed numbers in a list of numbers. [Note:- Consider 0th index as even indexed]
# # Sample Input
#  list1 = [2, 4, 3, 9, 13, 12, 7, 6, 1, 5]
# # Expected Output
#  -10
list1 = [2, 4, 3, 9, 13, 12, 7, 6, 1, 5]
sum_even = 0
sum_odd = 0
for i in range(len(list1)):
    print(i)
    if i % 2 == 0:
        sum_even += list1[i]
    else:
        sum_odd += list1[i]
difference = sum_even - sum_odd
print(difference)

# Write a program to print the list of numbers which are greater than the average of numbers in the following list.
# # Sample Input
#  list1 = [2, 4, 3, 9, 13, 12, 7, 6, 1, 5]
# # Expected Output
#  [9, 13, 12, 7]
list1 = [2, 4, 3, 9, 13, 12, 7, 6, 1, 5]
average = sum(list1) / len(list1)
greater_numbers = []
for num in list1:
    if num > average:
        greater_numbers.append(num)
print(greater_numbers)

# Write a program to print a new list containing squares of each element in the following list.
# # Sample Input
#  list1 = [3, 7, 11, 12, 17, 21]
# # Expected Output
#  list2 = [9, 49, 121, 144, 289, 441]
list1 = [3, 7, 11, 12, 17, 21]
list2 = []
for num in list1:
    square = num ** 2
    list2.append(square)
print(list2)

# Write a program to know how many times an element occurred in the list.
# # Sample Input
#  list1 = [5, 10, 15, 20, 25, 50, 20]
#  element = 20 # Expected Output
#  2
list1 = [5, 10, 15, 20, 25, 50, 20]
element = 20
count = 0
for num in list1:
    if num == element:
        count += 1
print(count)

# Given a Python list, write a program to find the value 20 in the list, and if it is present, replace the first occurrence of a value with 200.
# # Sample Input
#  list1 = [5, 10, 15, 20, 25, 50, 20]
# # Expected Output
#  list1= [5, 10, 15, 200, 25, 50, 20]
list1 = [5, 10, 15, 20, 25, 50, 20]
index = list1.index(20)
list1[index] = 200
print(list1)

# Given an input list, write a program to remove the element at index 4 and add it to the 2nd position and also, at the end of the list.
# # Sample Input
#  list1= [54, 44, 27, 79, 91, 41]
# # Expected Output
#  list1= [34, 54, 11, 67, 89, 43, 94, 11]
list1 = [54, 44, 27, 79, 91, 41]
removed_element = list1.pop(4)
list1.insert(2, removed_element)
list1.append(removed_element)
print(list1)

# Two lists are given below. Write a program to create a third list by picking an odd-index element from the first list and even index elements from second.
# # Sample Input
#  list1 = [3, 6, 9, 12, 15, 18, 21]
#  list2 = [4, 8, 12, 16, 20, 24, 28]
# # Expected Output
#  list3 = [6, 12, 18, 4, 12, 20, 28]
list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
list3 = []
for i in range(1, len(list1), 2):
    list3.append(list1[i])
for i in range(0, len(list2), 2):
    list3.append(list2[i])
print(list3)

# Write a program to add 7000 after 6000 in the following list.
# # Sample Input
#  list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# # Expected Output
#  list1 = [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
sublist = list1[2][2]
sublist.append(7000)
print(list1)
