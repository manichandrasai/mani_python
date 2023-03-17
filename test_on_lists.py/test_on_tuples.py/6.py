l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
m = []
for i in (l1[1::2]):
    m.append(i)
for i in (l2[0::2]):
    m.append(i)
print(m)    
         
