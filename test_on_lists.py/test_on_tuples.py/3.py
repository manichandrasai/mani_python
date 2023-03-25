students = [
 	("John", ["Computers", "Physics", "Maths"]), 
	("Wasim", ["Maths", "Computers", "Statistics"]), 
	("Naresh", ["Computers", "Accounting", "Economics"]), 
	("SaiTeja", ["English", "Accounting", "Economics", "Law"]), 
	("Sravani", ["Sociology", "Economics", "Law", "Stats", "Music"])
	]
v = 0
for name, sub in students:
    if "Computers" in sub:
        v += 1
print(f"the no students who has computers has one sub is{v}")        