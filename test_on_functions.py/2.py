# The goal of this challenge is to analyze a string to check if it contains two of the same letter in a row. For example, the string "hello" has l twice in a row, while the string "nono" does not have two identical letters in a row. Define a function named double_letters that takes a single parameter. The parameter is a string. Your function must return True if there are two identical letters in a row in the string, and False otherwise.

def double_letters(str):
    for i in range(len(str)-1):
        if str[i]== str[i+1]:
            return True
    return False
res_1 = double_letters("hello")
print(res_1)
res_2 = double_letters("nono")
print(res_2)

     