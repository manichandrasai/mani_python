database = []
n = int(input("enter no of records:"))
for id in range(1001,1001+n):
    name = input("enter name:")
    salary = float(input("enter salary:"))
    phno = int(input("enter a num:"))
    record = (id,name,salary,phno)
    database.append(record)
print(database)    