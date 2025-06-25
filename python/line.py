#file i/0

#open,with,readline

with open("names.txt", "r") as file: #a=append
    lines = file.readlines()

for line in lines:
    print("hello,", line, end="") #both are  same (any one is enough)
    print("hello,", line.rstrip()) #both are same