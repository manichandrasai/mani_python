# ------ question 1
# 1. Write a function that returns the common elements between two given lists.
def common_element(l1,l2):
    '''
    This function return the common elements between 
    two given lists

    Parameters:
        l1 : list of numbers
        l2 : list of numbers

    Returns:
        This will return the common elements in given lists
    '''
    return  list(set(l1).intersection(l2))

l1 = [2,3,5,6]
l2 = [3,8,5,7]
print(common_element(l1,l2))


# ----- question 2
"""2. Given a list of n tuples, where each tuple contains 3 elements.
 Write a function that return the sorted list of tuples based on second element in each tuple."""

def sorted_list_tuples_second_element(elements):
    '''
    This function will return the sorted list of tuples based on second elements

    Parameters:
        elements : list of tuples(each tuple contains 3 elements)
    Returns:
        this will return the sorted list of tuples based on 2nd element in tuple
    '''
    return sorted(elements,key = lambda x:x[1])

elements = [("abc",99,39000.03),("xyz",23,33000.23),("pqr",88,35000.5)]
print(sorted_list_tuples_second_element(elements))


# ----- question 3
# 3. Write a function that returns the second highest number in a list.
def second_highest(numbers):
    sorted_numbers = sorted(set(numbers))
    if len(sorted_numbers) < 2:
        return None
    else:
        return sorted_numbers[-2]
    '''
    This function will return second highest number in a given list

    Parameters:
        l : list of numbers

    Returns: 
        This will return the second highest number from the given list

    '''    
l = [1,2,3,4,5]
print(second_highest(l))

# ----------- question 4
# 4. Write a function that returns the first non-repeating character in a string.

def first_non_repeating_char(string):
    '''
    This function will return the first non repeating character in string

    Parameters:
        input_string : string

    Returns:
        this will return the non repeating character

    '''
    for char in string:
        if string.count(char) == 1:
            return char
    return None

# Calling function
input_string = "abracadabra"
result = first_non_repeating_char(input_string)
print(result)

# ------ question 5
# 5. Write a function that checks if two strings (for example, listen and silent) are anagrams of each other.
 
def check_two_strings(s1, s2):
    '''
    This function will check given 2 strings are anagrams of each other

    Parameters : 
        s1 : string
        s2 : string
    
    Returns:
        return the given strings are anagrams of each other or not
    '''
    if(sorted(s1) == sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")        
         
s1 ="listen"
s2 ="silent"
check_two_strings(s1, s2)
