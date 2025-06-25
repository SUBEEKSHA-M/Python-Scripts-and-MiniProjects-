class Wizard:
    def __init__(self, name, patronus=None):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} (Patronus: {self.patronus or 'Unknown'})"

class Student(Wizard):
    def __init__(self, name, house, patronus=None):
        super().__init__(name, patronus)
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house} house (Patronus: {self.patronus or 'Unknown'})"

class Professor(Wizard):
    def __init__(self, name, subject, patronus=None):
        super().__init__(name, patronus)
        self.subject = subject

    def __str__(self):
        return f"Professor {self.name}, teaches {self.subject} (Patronus: {self.patronus or 'Unknown'})"

wizard = Wizard("Albus", "Phoenix")
student = Student("Harry", "Gryffindor", "Stag")
professor = Professor("Severus", "Defense Against the Dark Arts", "Doe")

print(wizard)
print(student)
print(professor)
