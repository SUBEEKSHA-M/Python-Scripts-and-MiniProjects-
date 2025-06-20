#file i/0

#open

name = input("what's your name? ")

file = open("names.txt", "a")  #a=append
file.write(f"{name}\n")
file.close()