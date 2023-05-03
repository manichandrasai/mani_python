class Employee:    
    id = 42 
    name = "Mani"    
    def display (self):    
        print(self.id,self.name)  
c1 = Employee()
print(c1)    

class car:  
    def __init__(x,modelname, year):  
        x.modelname = modelname  
        x.year = year  
    def display(x):  
        print(x.modelname,x.year)  
  
c1 = car("Toyota", 2016) 
c2 = car("Benz", 2020)  

c1.display() 
c2.display()   

# class Student:    
#     count = 0    
#     def __init__(self):    
#         Student.count = Student.count + 1    
# s1=Student()    
# s2=Student()    
# s3=Student()    
# print("The number of students:",Student.count)  
