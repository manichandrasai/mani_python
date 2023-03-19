n = int(input("enter number of calls:"))
if (n <= 100):
    bill = 200
    print("the telephone bill is Rs", bill)
if (n  > 100 and n <= 150):
    bill = 200 + 0.60*(n-100)
    print("the telephone bill is Rs", bill)
if(n>150 and n <= 200):
    bill = 200 + (0.60*50) +0.50*(n-150)
    print("the telephone bill is Rs ", bill)
if(n > 200):
    bill = 200 + (0.60*50) + (0.50*50 )+ 0.40*(n-200) 
    print("the telephone bill is Rs", bill)




