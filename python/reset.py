# regression expression

import re  #re.search(pattern, string, flags=0)

email = input("What's your email?").strip()

if re.search("@", email):
    print("Valid")
else:
    print("Invalid")

#re= repetitions

# .     any character except a newline 
# *     0 or more repetitions  
# +     1 or more repetitions
# ?     0 or 1 repetition
# {m}   m repetitions
# {m,n} m-n repetitions

email = input("What's your email?").strip()

if re.search(".*@.*", email):
    print("Valid")      #abc@gmail.com  #subee@
else:
    print("Invalid")

# .+@.+

email = input("What's your email?").strip()

if re.search(".+@.+", email):
    print("Valid")      #abc@gmail.com 
else:
    print("Invalid")    #subee@

# .+@.+.edu

email = input("What's your email?").strip()

if re.search(".+@.+.edu", email):
    print("Valid")      #abc@gmail.edu  #abc@gmail?edu
else:
    print("Invalid")    #subee@

# ^  matches the start of the string
# $  matches the end of the string jst before the newline at the end of the string

email = input("What's your email?").strip()

if re.search(r"^.+@.+\.edu$", email):
    print("Valid")      #My email is subee@hard.edu.
else:
    print("Invalid")

# []   set of characters
# [^]  complementing the set

email = input("What's your email?").strip()

if re.search(r"^[^@]+@[^@]+\.edu$", email):
    print("Valid")      # .edu@something.edu
else:
    print("Invalid")    #subee@@@hardvard.edu

# [a-zA-Z0-9_]

email = input("What's your email?").strip()

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.eu$", email):
    print("Valid")      # subee_ksha@hardvard.edu
else:
    print("Invalid")    # subee@@@hardvard.edu

# \d  decimal digit
# \D  not a decimal digit
# \s  whitespace characters
# \S  not a whitespace character
# \w  word character ... as well as numbers and the underscore
# \W  not a word character

email = input("What's your email?").strip()

if re.search(r"^\w+@\w+\.edu$", email):
    print("Valid")
else:
    print("Invalid")    #subee@@@hardvard.edu

# A|B     either A or B
#(...)    a group
#(?:...)  non-capturing version

email = input("What's your email?").strip()

if re.search(r"^\w+@\w+\.(com|edu|gov|net|org)$", email):
    print("Valid")           # subee_ksha@hardvard.edu
else:
    print("Invalid") 