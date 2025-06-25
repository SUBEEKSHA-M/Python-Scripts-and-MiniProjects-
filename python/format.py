# matches

import re
name = input("what is your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)
if matches:
    last, first = matches.groups()
    name = f"{first} {last}"
print(f"hello, {name}")

#output: what is your name? muruganantham subee
#                           hello, subee muruganantham

#-------------------#

# :=

import re

name = input("What is your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")

#both o/p are same