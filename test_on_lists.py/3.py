m = []
for i in range(6):
    n = int(input("enter num:"))
    m.append(n)
print(m)
m.sort()
print(" the largest number in the given list" , m[-1])