n = int(input("enter a num:"))
i = 2
rt = int(n**.5)
while i <= rt:
    if n % i == 0:
        print("not prime")
        break
    i += 1
else:
    print("prime")    