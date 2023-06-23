# ----------Practice Questions----------
# Write a program to create the set {'cat', 1, 2, 3}.
my_set = {'cat', 1, 2, 3}
print(type(my_set))

# Write a program to find the length of a set {'c', 'a', 't', '1', '2', '3'}.
my_set = {'c', 'a', 't', '1', '2', '3'}
length = len(my_set)
print(length)

# Write a program to add member(s) in a set.
# # Input
# set1 = {'Blue'}
# set2 = {'Green', 'Yellow'}
# # Expected Output
# {'Blue', 'Green', 'Yellow'}
set1 = {'Blue'}
set2 = {'Green', 'Yellow'}
set1.add('Red')

set1.update(set2)
print(set1)

# Write a program to remove an item from a set if it is present in the set.
# # Input
# set1 = {0, 1, 2, 3, 4, 5}
# discard_value = 4
# # Expected Output
# {0, 1, 2, 3, 5}
set1 = {0, 1, 2, 3, 4, 5}
discard_value = 4
set1.discard(discard_value)
print(set1)

# Write a program to find maximum and the minimum value in a set.
# # Input
# set1 = {5, 10, 3, 15, 2, 20}
# # Expected Output
# max = 20
# min = 2
set1 = {5, 10, 3, 15, 2, 20}
max_value = max(set1)
min_value = min(set1)
print("Max =", max_value)
print("Min =", min_value)


# Write a program to remove all duplicates from a list using sets.
# # Input
# [2, 3, 4, 2, 7, 3, 4, 8, 9, 1, 2, 3]
# # Expected output
# {1, 2, 3, 4, 7, 8, 9}
input_list = [2, 3, 4, 2, 7, 3, 4, 8, 9, 1, 2, 3]
unique_set = set(input_list)
output_list = list(unique_set)
output_list.sort()
print(output_list)


# Write a program to create a set containing the frozenset fs, it should look like {frozenset({'cat', 2, 3, 1})}.
fs = frozenset({'cat', 2, 3, 1})
set_with_frozenset = {fs}
print(set_with_frozenset)
