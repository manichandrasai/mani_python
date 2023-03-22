a = []
n = int(input("enter a num:"))
for i in range(n):
    word = input("enter a word:")
    num = int(input("enter a num:"))
    a.append((word,num))
print(a)
for i in a:
    print(i[0])