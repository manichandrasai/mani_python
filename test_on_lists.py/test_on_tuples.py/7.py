l1 = [1, 2, 3, 4]
l2 = [1, 2]
# m = []
# for i in l1:
#     if i not in l2:
#         m.append(i)
# print(m)        


m = (list(set(l1)-set(l2)))
print(m)
