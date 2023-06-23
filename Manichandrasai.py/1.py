# Write a program to accept a number from the keyboard and if the number is even, print "EVEN" otherwise print "ODD".
m = int(input("enter a num:"))
if m % 2 == 0:
    print("given num is even")
else:
    print("given num is even")


# Write a program to take a line of text and a string and print "True" if the string exits in the line of text otherwise print "False".
line_of_text = input("Enter a line of text: ")
search_string = input("Enter a string to search for: ")
if search_string in line_of_text:
    print("True")
else:
    print("False")

# Write a program that asks the user to enter a word and prints out whether that word contains any vowels.
word = input("Enter a word: ")
vowels = False
if 'a' in word or 'e' in word or 'i' in word or 'o' in word or 'u' in word:
    vowels = True

if vowels:
    print("The word contains vowels.")
else:
    print("The word does not contain any vowels.")

# Write a program to check whether an alphabet is a vowel or consonant.
alphabet = input("enter a alphabet:")
if alphabet.isalpha() and len(alphabet) == 1:
    if alphabet in "aeiou" or alphabet in "AEIOU":
        print("the alphabet is vowel")
    else:
        print("alphabet is not vowel")    


# Write a program that asks the user for two numbers and prints Close if the numbers are within .001 of each other and Not close otherwise.
num1 = float(input("enter a num:"))
num2= float(input("enetr a num:"))
if abs(num1 - num2) <= 0.001:
    print("close")
else:
    print("not close")

# Write a program to take input of age of 3 people from user and determine the oldest and the youngest among them.
age1 = int(input("enter age1:"))
age2 = int(input("enter age2:"))
age3 = int(input("enter age3:"))

if age1>age2 and age1>age3:
    print("age 1 is older among all")
elif age2>age1 and age2>age3:
    print("age 2 is older among all")   
else:
    print("age 3 is older among all")   
# younger
if age1 < age2 and age1 < age3:
    print("age 1 is younger among all") 
elif age2 < age1 and age2 < age3:
    print("age 2 is younger among all") 
else:
    print("age 3 is younger among all") 


# Write a program to accept maximum of 6 digits number and print out the sum of even digits of that number and multiplication of odd digits of that number.
number = int(input("Enter a maximum 6-digit number: "))

even_sum = 0
odd_product = 1

while number > 0:
    digit = number % 10

    if digit % 2 == 0:
        even_sum += digit
    else:
        odd_product *= digit

    number //= 10

print("Sum of even digits:", even_sum)
print("Multiplication of odd digits:", odd_product)


# Write a program to check whether the given year is leap year or not.
year = int(input("enter the year:"))
if year % 4 == 0  and (year % 100 != 0 or year % 400 == 0):
    print("this is a leap year")
else:
    print("this is a  not a leap year") 

# Write a program to check a triangle is equilateral, isosceles or scalene.
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

if side1 == side2 == side3:
    print("The triangle is equilateral.")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")

# Write a program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700.
for num in range(1500, 2701):
    if num % 7 == 0 and num % 5 == 0:
        print(num)
# Write a program to prompt the user for a temperature and what units (Celsius or Fahrenheit) the temperature is in and print the temperature by converting into the other unit. [Hint:- F = 95 C + 32 and C = 9 5 (F − 32)]
char = input("enter the char")
F = float(input("enter the temperature "))
if char == 'C':
    C = (95*(F - 32))
    print(C)
 
# A store charges Rs.12 per item if you buy less than 10 items. If you buy between 10 and 99 items, the cost is Rs.10 per item. If you buy 100 or more items, the cost is Rs.7 per item. Write a program that asks the user how many items they are buying and prints the total cost.
n = int(input("how many items u wanted to buy:"))
if(n < 10):
    print(f"the total cost of items is {n*12} ")
if(n >= 10 and n < 100 ):
    print(f"the total cost of items is {n*10} ")
if(n > 100):
    print(f"the total cost of items is {n*7} ")

# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Write a program that prompt the user for their salary and year of service and print the net bonus amount.
salary = int(input("enter the salary:"))
year_of_exp = int(input("enter the year of exp:"))
bonus = 5
min_work_exp = 5
if year_of_exp > min_work_exp:
    bonus = (salary*bonus)/100
    print(f"the bonus amount is {bonus}")
else:
    print(f"you are not eligible")    

# A shop will give discount of 10% if the cost of purchased quantity is more than 1000. Suppose, one unit will cost 100. Write a program to prompt the user for quantity and print the total cost for user.
unit_cost = 100
m = int(input("enter the amount of units:"))
total_cost = (unit_cost * m)
if total_cost> 1000:
    discount = (total_cost*10)/100
    print(f"the discount is {discount}")
else:
    print(f"no discount")    