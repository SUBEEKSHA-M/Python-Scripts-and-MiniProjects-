Students={
    "Subee": "Tamilnadu",
    "Dharma": "Bangalore",
    "Yalini": "Tamilnadu"
}

print(Students)

for Student in Students:
    print(Student, Students[Student])

for Student in Students:
    print(Student, Students[Student], sep=": ")
