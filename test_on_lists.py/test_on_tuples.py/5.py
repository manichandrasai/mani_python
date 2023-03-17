t1 = (3, 4, 5, 6)
t2 = (5, 7, 4, 10)
m = []
for i in t1:
    if i not in t2:
        m.append(i)       
for i in t2:
    if i not in t1:
        m.append (i)
print(tuple(m))        

