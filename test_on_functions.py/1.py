# 1. Write a function named type_check that takes two parameters and it should return True if both parameters are of the same data type, and False otherwise.
# For example, calling type_check(1, 2) should return True, while calling type_check("a", 1) should return False.

def type_check(a,b):
    return type(a) == type(b)
result_1 = type_check(1,2)
result_2 = type_check("a",1)
print(result_1,result_2)



