a = []
n = int(input("enter a num:"))
for i in range(n):
    word = input("enter a word:")
    num = int(input("enter a num:"))
    a.append((word,num))
print(a)
m = []
for i in a:
    if(i[1] % 2!= 0):
        m.append((i[0],i[1]))
print(m)        