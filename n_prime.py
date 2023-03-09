n = int(input("enter a num:"))
i = 1
c = 0
while i <= n:
    if n  % i == 0:
        c += 1
    i += 1
if c == 2:
    print("prime number")    
else:
    print(" not prime")            