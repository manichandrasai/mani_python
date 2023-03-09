l = [2,3,4,5,4,3,2,1,4,5,6,7,8]
m = []
for i in l:
    print(i, end =" ")
    if( i not in m):
        m.append(i)
print(m)    