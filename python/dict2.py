students=[
    {"name": "Subee", "student": "Tamilnadu", "language": "Tamil, English"},
    {"name": "Dharma", "student": "Bangalore", "language": "Kannadam, English"},
    {"name": "Rajii", "student": "Tamilnadu", "language": "Tamil, English"},
    {"name": "Yalini", "student": "Kerala", "language": None},
]

for student in students:
    print(student["name"])

    print(student["name"], student["student"], student["language"], sep=", ")