# f = open("data.csv","r")
# s = f.read()
# f.close()
# # print(s)
n = int(input("enter a num:"))
for i in range(2,n):
    if n % i == 0:
        print("not prime")
else:
    print("prime")    
