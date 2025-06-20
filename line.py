#file i/0

#open,with,readline

with open("names.txt", "r") as file: #a=append
    lines = file.readlines()

for line in lines:
    print("hello,", line, end="")