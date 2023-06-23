# # 1
# # * 
# # * * 
# # * * * 
# # * * * * 
# # * * * * * 
# for i in range (1,6):
#     for j in range(1,i+1):
#         print("*",end = " ")
#     print()

# # # 2
# # 1 
# # 1 2 
# # 1 2 3 
# # 1 2 3 4 
# # 1 2 3 4 5 
# for i in range (1,6):
#     for j in range(1,i+1):
#         print(j ,end = " ")
#     print()

# # # 3
# # 1 
# # 2 2 
# # 3 3 3 
# # 4 4 4 4 
# # 5 5 5 5 5 
# for i in range (1,6):
#     for j in range(1,i+1):
#         print(i ,end = " ")
#     print() 

# # # 4
# # 5 
# # 4 4 
# # 3 3 3 
# # 2 2 2 2 
# # 1 1 1 1 1 
# for i in range (5,0,-1):
#     for j in range(5,i-1,-1):
#         print(i ,end = " ")
#     print() 

# # # 5
# # 5 
# # 5 4 
# # 5 4 3 
# # 5 4 3 2 
# # 5 4 3 2 1 
# for i in range (5,0,-1):
#     for j in range(5,i-1,-1):
#         print(j ,end = " ")
#     print() 

# # # 6
# # 5 5 5 5 5 
# # 4 4 4 4 
# # 3 3 3 
# # 2 2 
# # 1 
# for i in range (5,0,-1):
#     for j in range(5,5-i,-1):
#         print(i ,end = " ")
#     print() 

# # # 7
# # 1 
# # 2 3 
# # 4 5 6 
# # 7 8 9 10 
# # 11 12 13 14 15 
# c = 1
# for i in range (5,0,-1):
#     for j in range(5,i-1,-1):
#         print(c ,end = " ")
#         c += 1
#     print() 

# # # 8 
# # 9 7 5 3 1 
# # 9 7 5 3 
# # 9 7 5 
# # 9 7 
# # 9 
# for i in range (9 ,0, -2):
#     for j in range(9, 9-i,-2):
#         print(j ,end = " ")
#     print() 

# # 9
# # 9 
# # 9 7 
# # 9 7 5 
# # 9 7 5 3 
# # 9 7 5 3 1 
# for i in range (5,0,-1):
#     for j in range(5,i-1,-1):
#         print(((2*j)-1) ,end = " ")
#     print() 

# #10
# # 1 3 5 7 9 
# # 1 3 5 7 
# # 1 3 5 
# # 1 3 
# # 1 
# for i in range (5 , 0, -1):
#     for j in range(1,i+1):
#         print(((2*j) -1),end = " ")
#     print()


# def is_prime(n):
#     if n <= 1:
#         return False
#     rt = int(n**.5)
#     for i in range(2,rt+1):
#         if n % i == 0:
#             return "not prime"
#         return "prime"
# n = int(input("enter a num:"))
# print(is_prime(n))
    
    
# for i in range (5 , 0, -1):
#     for j in range(1,i+1):
#         print(((2*j) -1),end = " ")
#     print()

# def pattern(n):
#   for i in range (1,n):
#     for j in range(1,i+1):
#         print(((2*j) -1),end = " ")
#     print()    
# n = int(input("enter a num:"))
# pattern(n)

# def pattern(n):
#     space = 0
#     m = 1
#     for i in range(n,0,-1):
#             print(space*''+ i*str(m))
#             space += 1
#             m += 1
            
# n = int(input("enter a num:"))
# pattern(n)


def pattern(n):
    space = 0
    m = n
    for i in range(n, 0, -1):
        print(space * ' ' + str(i) * i)
        space += 1
        m -= 1

n = int(input("Enter a number: "))
pattern(n)
