# t = int(input("enter n:"))
t = (76,98,55,45,42,45)
m = []
for i in t:
    if(i  not in m):
        m.append(i)
print(tuple(m))       