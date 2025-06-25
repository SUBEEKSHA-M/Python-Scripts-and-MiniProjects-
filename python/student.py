# part of detail.py

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["India", "America", "Australia", "Japan"]:  
            raise ValueError("Invalid house")  # ✅ Typo fixed
        self.name = name
        self.house = house

def main():
    try:
        student = get_student()
        print(f"{student.name} from {student.house}")
    except ValueError as e:
        print(f"Error: {e}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()

# part of detail.py

class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["India", "America", "Australia", "Japan"]:  
            raise ValueError("Invalid house")  # ✅ Typo fixed
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    def charm(self):
        match self.patronus:
            case "Stag":
                return "*"
            case "Otter":
                return "&"
            case "Jack Rissell terrier":
                return "^"
            case _:
                return "/"
def main():
        student = get_student()
        print("Expecto Patronum!")
        print(student.charm)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()

