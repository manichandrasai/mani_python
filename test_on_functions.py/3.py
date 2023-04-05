# Write a function to find the sum of the cube of elements in a list. The list is received as an argument to the function and it should return the sum.
def cube_of_elements(l):
    sum = 0
    for i in l:
        sum += i**3
    return sum
res = cube_of_elements([1,2,3,4,5])
print(res)  