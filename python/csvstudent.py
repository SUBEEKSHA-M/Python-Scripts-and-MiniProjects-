#same as the students.py
#here import csv

import csv
csvstudent=[]

with open("csvstudent.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        csvstudent.append({"name": name, "home": home})

for student in sorted (csvstudent, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")