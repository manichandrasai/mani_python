t = (1, 2, 3, 4, 5, 6, 7, 8, 9)
m = []
c = 0
n = []
v = 0
for i in t:
    if (i % 2 == 0):
        m.append(i)
        c += 1
    else:
        n.append (i)
        v += 1
print(tuple(m))
print(tuple(n))
print(f"number of even numbers:{c}")      
print(f"number of odd numbers:{v}")  



