# Write a function half_and_half that takes in a list and change the list such that the elements of the second half are now in the first half. For example, if the list is [10,20,30,40,50,60], then it should return [40,50,60,10,20,30] and if the list is [10,20,30,40,50,60,70], then it should return [50,60,70,40,10,20,30].
def half_and_half(lst):
    length = len(lst)
    mid = length // 2  # Get the index of the middle element
    if length % 2 != 0:
        mid += 1  # If the list has an odd length, increment the middle index by 1
    lst[:] = lst[mid:] + lst[:mid]  # Slice and concatenate to rearrange the list
    return lst
# Example 1
lst1 = [10, 20, 30, 40, 50, 60]
result1 = half_and_half(lst1)
print(result1)  # Output: [40, 50, 60, 10, 20, 30]

# Example 2
lst2 = [10, 20, 30, 40, 50, 60, 70]
result2 = half_and_half(lst2)
print(result2)  # Output: [50, 60, 70, 40, 10, 20, 30]
