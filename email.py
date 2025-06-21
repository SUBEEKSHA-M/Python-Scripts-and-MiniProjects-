#Regression expression

#also called regexes

email = input("What's your email?").strip()

if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")

#split()

email = input("What's your email?").strip()

username, domain = email.split("@")

if username and "." in domain:
    print("Valid")
else:
    print("Invalid")   #abc@def

#domain.endswith()

email = input("What's your email?").strip()

username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("Valid")    #abc@.edu
else:
    print("Invalid")