n = int(input("enter the temp:"))
if (n<-273.15):
    print("invalid")
elif (n==-273.15):
    print("absolute 0")
elif (n>-273.15 and n<0):
    print("temperture is below freezing point")
elif (n==0):
    print("freezing point")
elif (n>0 and n<100):
    print("temperature is normal range")
elif (n==100):
    print("temperature is boiling point")    
elif (n>100):
    print("boiling point") 