import csv
name = input("what is your name?")
home = input("where's your home?")

with open("stu1write.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])