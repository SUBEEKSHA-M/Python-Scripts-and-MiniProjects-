name = input("Name: ")
house = input("House: ")
print(f"{name} from {house}")

#tuple

def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House:")
    return (name, house)

if __name__=="__main__":
    main()

#other method 1

def main1():
    student = get_student()
    print(f"{student['name']} from {student['house']}")

def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House:")
    return student

if __name__=="__main__":
    main1()

#other method 2

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    student = student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

if __name__=="--main__":
    main()