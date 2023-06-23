#------------- Practice Questions----------
# Write a program to prompt the user to give name and marks of 5 different students, store them in dictionary and print it after sorting the dictionary with respect to their marks.
student ={}
for i in range(6):
    name = input("enter the name :")
    marks = int(input("enter the marks:"))
    student[name] = marks
print(student)    
print(sorted(student.items(),key = lambda x:x[1]))
# Use the dictionary given below whose keys are month names and whose values are the number of days in the corresponding months.
# (a) Ask the user to enter a month name and use the dictionary to tell them how many days are in the month.
# (b) Print out all of the keys in alphabetical order.
# (c) Print out all of the months with 31 days.
# days = { ' January ' : 31, ' February ' : 28, ' March ' : 31, ' April ' : 30,
#  ' May ' : 31, ' June ' : 30, ' July ' : 31, ' August ' : 31,
#  ' September ' : 30, ' October ' : 31, ' November ' : 30, ' December ' : 31}

days = {
    'January': 31,
    'February': 28,
    'March': 31,
    'April': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'August': 31,
    'September': 30,
    'October': 31,
    'November': 30,
    'December': 31
}

# (a) Ask the user to enter a month name and print the number of days in that month
month_name = input("Enter a month name: ")
if month_name in days:
    print("Number of days in {}: {}".format(month_name, days[month_name]))
else:
    print("Invalid month name.")

# (b) Print out all of the keys in alphabetical order
sorted_keys = sorted(days.keys())
print("Months in alphabetical order:")
for month in sorted_keys:
    print(month)

# (c) Print out all of the months with 31 days
days = {
    'January': 31,
    'February': 28,
    'March': 31,
    'April': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'August': 31,
    'September': 30,
    'October': 31,
    'November': 30,
    'December': 31
}

months_with_31_days = []
for month, days in days.items():
    if days == 31:
        months_with_31_days.append(month)

print("Months with 31 days:")
for month in months_with_31_days:
    print(month)


# Write a program to count the number of characters (character frequency) in a string.
# # Sample Input
#  'google'
# # Expected Output
#  {'g': 2, 'o': 2, 'l': 1, 'e': 1}
string = 'google'
char_frequency = {}
for char in string:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
print(char_frequency)


# Write a program to count the number of occurrences of each letter in word "MISSISSIPPI". Store count of every letter with the letter in a dictionary and print the sorted dictionary according to the count of letters.

# Write a program to count the occurrences of each word in the text given below.
#  """Through three cheese trees three free fleas flew.
#  While these fleas flew, freezy breeze blew.
#  Freezy breeze made these three trees freeze.
#  Freezy trees made these trees' cheese freeze.
#  That's what made these three free fleas sneeze."""
text = """Through three cheese trees three free fleas flew.
While these fleas flew, freezy breeze blew.
Freezy breeze made these three trees freeze.
Freezy trees made these trees' cheese freeze.
That's what made these three free fleas sneeze."""

word_count = {}

# Remove punctuation and convert text to lowercase
cleaned_text = text.replace(".", "").replace(",", "").replace("'", "").lower()

# Split the text into words
words = cleaned_text.split()

# Count occurrences of each word
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print the word count
for word, count in word_count.items():
    print(f"{word}: {count}")


# Write a program to get the frequency of the elements in a list.
# # Sample Input
#  [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]
# # Expected Output
#  {10 : 4, 20 : 4, 40 : 2, 50 : 2, 30 : 1}
lst = [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]
element_frequency = {}
for element in lst:
    if element in element_frequency:
        element_frequency[element] += 1
    else:
        element_frequency[element] = 1

print(element_frequency)


# Write a program to concatenate following dictionaries to create a new one.
# # Sample Input
#  dic1 = {1 : 10, 2 : 20}
#  dic2 = {3 : 30, 4 : 40}
#  dic3 = {5 : 50, 6 : 60}
# # Expected Output
#  {1 : 10, 2 : 20, 3 : 30, 4 : 40, 5 : 50, 6 : 60}
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

new_dict = {}

# Concatenate dictionaries
new_dict.update(dic1)
new_dict.update(dic2)
new_dict.update(dic3)

print(new_dict)

square_dict = {}

for num in range(1, 16):
    square_dict[num] = num ** 2

print(square_dict)

# Write a Python program to print the sum all the values in a dictionary.
# # Sample Input
#  {'data1' : 100, 'data2' : 54,'data3' : 247}
# # Expected Output
#  293
data = {'data1': 100, 'data2': 54, 'data3': 247}
sum_values = sum(data.values())
print(sum_values)


# Write a program that reads through any dictionary given below and prints the following:
# (a) All the users whose phone number ends in an 8
# (b) All the users that don’t have an email address listed
# d = [
#  { ' name ' : ' Todd ' , ' phone ' : ' 555-1414 ' , ' email ' : ' todd@mail.net ' },
#  { ' name ' : ' Helga ' , ' phone ' : ' 555-1618 ' , ' email ' : ' helga@mail.net ' },
#  { ' name ' : ' Princess ' , ' phone ' : ' 555-3141 ' , ' email ' : '' },
#  { ' name ' : ' LJ ' , ' phone ' : ' 555-2718 ' , ' email ' : ' lj@mail.net ' }
#  ]

d = [
    {'name': 'Todd', 'phone': '555-1414', 'email': 'todd@mail.net'},
    {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
    {'name': 'Princess', 'phone': '555-3141', 'email': ''},
    {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@mail.net'}
]

# Users whose phone number ends in an '8'
print("Users whose phone number ends in an '8':")
for user in d:
    if user['phone'][-1] == '8':
        print(user['name'])

# Users who don't have an email address listed
print("\nUsers who don't have an email address listed:")
for user in d:
    if user['email'] == '':
        print(user['name'])
