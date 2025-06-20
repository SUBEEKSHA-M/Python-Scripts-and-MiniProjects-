try:
    x= int(input("What is x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an interger")

#else

try:
    x= int(input("What is x? "))
except ValueError:
    print("x is not an interger")
else:
    print(f"x is {x}")

#while

while True:
    try:
     x= int(input("What is x? "))
    except ValueError:
        print("x is not an interger")
    else:
        break
print(f"x is {x}")

#break

while True:
    try:
        x= int(input("What is x? "))
        break
    except ValueError:
        print("x is not an interger")
print(f"x is {x}")

#def function

def main():
    x=get_int()
    print(f"x is {x}")

def get_int():

    while True:
        try:
            x= int(input("What is x? "))
        except ValueError:
            print("x is not an interger")
        else:
            break
    return x

main()

#pass

def main1():
    x=get_int()
    print(f"x is {x}")

def get_int():

    while True:
        try:
            return int(input("What is x? "))
        except ValueError:
            pass
main1()