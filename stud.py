#same as students but in dict

import csv
stud = []
with open("stud.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        stud.append({"name": row["name"], "home": row["home"]}) 
for student in sorted(stud, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")