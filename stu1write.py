import csv
name = input("what is your name?")
home = input("where's your home?")

with open("stu1write.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])

#dictwriter

with open("stu1write.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name,"home": home})
