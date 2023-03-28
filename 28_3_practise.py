

qhub = {}
n = int(input("enter a num:"))
for i in range(n):
    key = input("enter :")
    value = int(input("enter a num:"))
    qhub[key] = value
print(qhub)    
q = {"apple" : 2, "orange": 3 , "pineapple" : 4}
n ={}
for i in q:
    n[i] = q[i]
print(n)   


q = {}
q["name"] = "mani"
q["email"] = "manichandrasaimani@gmail.com"
q["phone no"] = 8179445240
print(list(q.items()))
print(q)
for i in q:
    
    print(f"the dict is {i}:{q[i]}")

p = {}
p["name"] = "biriyani"
p["email"] = "biriyani@gmail.com"
p["phone no"] = 7729834342
print(p.get('names','key not exist'))


l = []
l.append(q)
l.append(p)
l.append((q,p))
print(l)
