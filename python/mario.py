#column
def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")

main()

#row
def main1():
    print_row(4)

def print_row(width):
    print("?" * width)

main1()        

#row and column

def main2():
    print_square(3)

def print_square(size):

    #For each row in square
    for i in range(size):
        
        #for each brick in row
        for j in range(size):
            print("#",end="")
        print()

main2()

def main3():
    print_square(3)

def print_square(size):

    for i in range(size):
        print("#" * size)

main3()