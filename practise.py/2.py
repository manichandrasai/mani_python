n = input("enter a string:")
m = []
for i in  range (len(n)):
        if(n[i].isupper()):
            m.append(i)
print((m))