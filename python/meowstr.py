#  -> str

def meow(n: int) -> str:
    return "meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")

#usage

import sys

if len(sys.argv) == 1:
    print("meow")                #python meowstr.py
else:
    print("usage: meowstr.py")   #python meowstr.py 2