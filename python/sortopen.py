#file i/o

#sort

names=[]
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")

#reverse

for name in sorted(names, reverse=True):
    print(f"hello, {name}")