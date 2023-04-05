# Write a function half_and_half that takes in a list and change the list such that the elements of the second half are now in the first half. For example, if the list is [10,20,30,40,50,60], then it should return [40,50,60,10,20,30] and if the list is [10,20,30,40,50,60,70], then it should return [50,60,70,40,10,20,30].
def half_and_half(l):
    m = []
    list1 = l[-3::1]
    list2 = l[-1:-5:-1]
    m.extend(list2)
    m.extend(list1)
    return m
res = half_and_half([10,20,30,40,50,60,70])
print(res)