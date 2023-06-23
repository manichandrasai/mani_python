# --------Practice Questions---------
# Write a program to insert a new element into tuple of elements at a specified position.
my_tuple = (1, 2, 3, 4, 5)
new_element = 45
index = 3

if index < 0 or index > len(my_tuple):
    print("Invalid index")
else:
    m = list(my_tuple)
    m.insert(index, new_element)
    s = tuple(m)
    print(s)

# Write a program to count the number of even and odd numbers from a tuple of numbers.
# # Input
# tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# # Expected Output:
# Number of even numbers: 5
# Number of odd numbers: 4
tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even_count = 0
odd_count = 0
for num in tuple1:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)

# Write a program to modify or replace an existing element of a tuple with a new element.
tuple1 = (1, 2, 3, 4, 5)
index = 2
new_element = 10
list1 = list(tuple1)
list1[index] = new_element
tuple2 = tuple(list1)
print("Original tuple:", tuple1)
print("Modified tuple:", tuple2)

# Write a program to find Dissimilar Elements in Tuples.
# # Input
# tuple 1 = (3, 4, 5, 6)
# tuple 2 = (5, 7, 4, 10)
# # Expected Output
# Dissimilar elements = (3, 6, 7, 10)
tuple1 = (3, 4, 5, 6)
tuple2 = (5, 7, 4, 10)
set1 = set(tuple1)
set2 = set(tuple2)
dissimilar_elements = set1.symmetric_difference(set2)
result_tuple = tuple(dissimilar_elements)
print("Dissimilar elements:", result_tuple)
#  ----------or----------
tuple1 = (3, 4, 5, 6)
tuple2 = (5, 7, 4, 10)
dissimilar_elements = []
for element in tuple1:
    if element not in tuple2:
        dissimilar_elements.append(element)

for element in tuple2:
    if element not in tuple1:
        dissimilar_elements.append(element)
result_tuple = tuple(dissimilar_elements)
print("Dissimilar elements:", result_tuple)


# Write a program for addition of tuples.
# # Input
# tuple1 = (10, 4, 5)
# tuple2 = (2, 5, 18)
# # Expected Output
# new_tuple = (12, 9, 23)
tuple1 = (10, 4, 5)
tuple2 = (2, 5, 18)
new_tuple = []
for i in range(len(tuple1)):
    sum_value = tuple1[i] + tuple2[i]
    new_tuple.append(sum_value)
new_tuple = tuple(new_tuple)
print("New tuple:", new_tuple)

# Write a program to remove duplicates from tuple.
tuple1 = (1, 2, 3, 2, 4, 5, 3, 6, 7, 6)
unique_tuple = tuple(set(tuple1))
print("Tuple with duplicates removed:", unique_tuple)

# Write a program to sort the following employ data (list of tuples) as per their salaries (each tuple represents employ ID, name, age and salary)?
# data = [(1234, 'Abishek' , 32, 35000), (4532, 'Barathi', 27, 29000), (3455, 'Charan', 31, 37000), (9863, 'Devi', 42, 52000), (4852, 'Eswar', 37, 56000), (6481, 'Fathima', 40, 65000), (2793, 'Ganesh', 28, 45000)]
data = [(1234, 'Abishek', 32, 35000), (4532, 'Barathi', 27, 29000), (3455, 'Charan', 31, 37000), (9863, 'Devi', 42, 52000), (4852, 'Eswar', 37, 56000), (6481, 'Fathima', 40, 65000), (2793, 'Ganesh', 28, 45000)]
sorted_data = sorted(data, key=lambda x: x[3])
print("Sorted employee data based on salary:")
for emp in sorted_data:
    print(emp)

# Write a program to count the number of students has computers a one subject from the data given below.
# students = [ ("John", ["Computers", "Physics", “Maths”]), ("Wasim", ["Maths", "Computers", "Statistics"]), ("Naresh", ["Computers", "Accounting", "Economics"]), ("SaiTeja", ["English", "Accounting", "Economics", "Law"]), ("Sravani", ["Sociology", "Economics", "Law", "Stats", "Music"])]

students = [
    ("John", ["Computers", "Physics", "Maths"]),
    ("Wasim", ["Maths", "Computers", "Statistics"]),
    ("Naresh", ["Computers", "Accounting", "Economics"]),
    ("SaiTeja", ["English", "Accounting", "Economics", "Law"]),
    ("Sravani", ["Sociology", "Economics", "Law", "Stats", "Music"])
]
count = 0
for student, subjects in students:
    if "Computers" in subjects:
        count += 1
print("Number of students with Computers as one subject:", count)
