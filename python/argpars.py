import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", help="number of times to meow")
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")

#in terminal we have to code (python argpars.py -h)

#add type=int

import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", help="number of times to meow", type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("meow")