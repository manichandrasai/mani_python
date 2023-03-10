m = []
for i in range(6):
    n = int(input("enter num:"))
    m.append(n)
print(m)
sum = (m[0::2])
print(sum)

for i in sum:
    print(i, end = " ")
res = (sum[0]+sum[1]+sum[2])
print(res, end= " ")
