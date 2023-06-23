# Read a number from the keyboard,# If the number is even, square it.# If the number is an odd multiple of 5, cube it.# If the number is odd non-multiple of 5, multiply it with 10.
n = int(input("enter the num:"))
if n % 2 == 0:
    print(f"hi {n**2}")
else:
    if n % 5 == 0:
        print(f"hii{n**3}")
    else:
         print(f"hiii{n*10}") 

# A student will not be allowed to sit in exam if his/her attendance is less than 75%. Write a program to take the number of classes held, the number of classes attended as inputs and calculate the percentage of class attended. If the user attendance is less than 75%, ask the user if he/she has medical cause or not ( 'Y' or 'N' ). If response is 'Y', print he/she is eligible to sit in the exam, otherwise print he/she is not eligible to sit in the exam.
class_conducted = int(input("enter the no of classes conducted:"))
class_attended =  int(input("enter the no of classes attended:"))
percentage = 75
attendance = (class_attended / class_conducted)* 100
if attendance < 75:
    char = input("enter the char:")
    if char == 'Y':
        print("she is eligible")
    else:
         print("she is not  eligible")

#   -----------   while    ------------ 
i = 0
s = "Manichandrasai"
while i!= len(s):
    print(s[:i+1])
    i+= 1

s = "Manichandrasai"
for i in range(len(s)):
    print(s[:i+1])


# Print all the numbers which end with 3 below 50.
i = 1
while i <= 50:
    if i% 10 == 3:
        print(i)
    i+= 1

for i in range(1,51):
    if i% 10 == 3:
        print(i)

# Print all the factors of given number and their count.
n = int(input("enter a num:"))
c = 0
i = 1
print(f"the factors of {n} are ")
while i <= n:
    if n%i == 0:
        print(i)
        c+= 1
    i+=1
print(f"the factor count of {n} is: {c}")


n = int(input("enter the number:"))
c = 0
print(f"the factors of {n} are ")
for i in range(1,n+1):
    if n%i == 0:
        print(i)
        c+= 1
print(f"the factor count of {n} is: {c}")


# Check whether the given number is prime number or not.
n = int(input("enter a num:"))
c = 0
i = 1
while i <= n:
    if n% i == 0:
        print(f"the number is {i}")
        c+=1
    i+= 1
if c == 2:
    print("prime")
else:
    print("not prime")            


n = int(input("Enter a number: "))
c = 0
print(f"The factors of {n} are:")
for i in range(1, n + 1):
    if n % i == 0:
        print(f"The number is {i}")
        c += 1

if c == 2:
    print("Prime")
else:
    print("Not prime")
        


# There will not be any factors for a number after n//2. Right? So, we can write the code as below.
n = int(input("enter a num:"))
c = 0
i = 2
while i <=  n//2:
    if n% i == 0:
        print(i)
        c+= 1
    i+= 1
if c == 0:
    print("prime")
else:
    print("not prime")            


n = int(input("Enter a number: "))
c = 0

print(f"The factors of {n} are:")
for i in range(2, n//2 + 1):
    if n % i == 0:
        print(i)
        c += 1

if c == 0:
    print("Prime")
else:
    print("Not prime")

# Theorem: A prime number doesn't have any factors from 2 to square root of itself.

n = int(input("enter a num:"))
c = 0
i = 2
rt = int(n**0.5)
while i <= rt:
    if n% i == 0:
        print(i)
        c+= 1
    i+= 1
if c == 0:
    print("prime")
else:
    print("not prime")            

n = int(input("Enter a number: "))
c = 0

print(f"The factors of {n} are:")
rt = int(n ** 0.5)
for i in range(2, rt + 1):
    if n % i == 0:
        print(i)
        c += 1

if c == 0:
    print("Prime")
else:
    print("Not prime")

# while-else
i = 1 
while i <= 5:  
    print(i)  
    i += 1 
else:
    print("The End")

#  -------------Practice Exercise------------
# Write a 'while' loop that prints integers from zero to 5.
# n = int(input("enter a num:"))
# i = 1
# while i<= n:
#     print(i)
#     i+=1

# Write a 'while' loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.
string = input("enter a string:")
length = len(string)
index = length -1
while index >= 0:
    print(string[index])
    index-= 1


string = input("Enter a string: ")
print("The characters of the string in reverse order are:")
for index in range(len(string) - 1, -1, -1):
    print(string[index])


# Write a program that asks the user to enter a number and prints out all the divisors of that number
# n = int(input("enter a num:"))
# i = 1
# while i<= n:
#     if n%i == 0:
#         print(i)
#     i+=1    

# num = int(input("Enter a number: "))
# print("The divisors of", num, "are:")
# for i in range(1, num + 1):
#     if num % i == 0:
#         print(i)


# Factorial of any number n is represented by n! and is equal to 1 * 2 * 3 * .... * (n-1) * n.
# E.g.-
#  4! = 1 * 2 * 3 * 4 = 24
#  3! = 3 * 2 * 1 = 6
#  2! = 2 * 1 = 2
# Also,
#  1! = 1
#  0! = 1
# Write a program to calculate factorial of any given number.      
num = int(input("Enter a number: "))
factorial = 1
while num > 0:
    factorial *= num
    num -= 1
print(f"The factorial is: {factorial}")

num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i
print("The factorial is:", factorial)

# Write a program to find greatest common divisor (GCD) or highest common factor (HCF) of given two numbers.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 < num2:
    smaller = num1
else:
    smaller = num2
hcf = 1
i = 1
while i <= smaller:
    if num1 % i == 0 and num2 % i == 0:
        hcf = i
    i += 1
print("The Highest Common Factor (HCF) of", num1, "and", num2, "is:", hcf)

# Write a program to take integer inputs from user until he/she presses q and print the average and product of all those numbers.
numbers = []
while True:
    num = input("Enter an integer (or 'q' to quit): ")
    if num.lower() == 'q':
        break
    numbers.append(int(num))
if numbers:
    average = sum(numbers) / len(numbers)
    product = 1
    for num in numbers:
        product *= num

    print("Average:", average)
    print("Product:", product)
else:
    print("No numbers entered.")


# Write a program to print whether the given number is a palindrome or not. [Hint: A palindrome is nothing but any number or a string which remains unaltered when reversed].
# Input1: 12321# Output: Yes, a Palindrome number# Input2: RACECAR# Output: Yes, a Palindrome string
input_value = input("Enter a number or string: ")
reversed_value = input_value[::-1]
if input_value == reversed_value:
    print("Yes, a Palindrome")
else:
    print("Not a Palindrome")
