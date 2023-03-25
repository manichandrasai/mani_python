a = []
n = int(input("enter a num:"))
for i in range(n):
    word = input("enter a word:")
    num = int(input("enter a num:"))
    a.append((word,num))
print(a)
m = []
for i in a:
    m.append((i,len(i)))
print(m)    

