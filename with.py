#file i/0

#open,with

name = input("what's your name? ")

with open("names.txt", "a") as file: #a=append
    file.write(f"{name}\n")
