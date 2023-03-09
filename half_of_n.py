n = int(input("enter a num:"))
i = 2
while i <= n//2:
    if n  % i == 0:
        print("not prime")
        break
    i += 1
else:
    print("prime")            