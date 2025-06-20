#try, except

import sys
try:
    print("hello, my name is", sys.argv[1] )
except IndexError:
    print("Too few arguments")

# if, elif, else

import sys

if len(sys.argv)<2:
    print("Too few arguments")
elif len(sys.argv)>2:
    print("Too large arguments")
else:
    print("hello, my name is", sys.argv[1])

# if, elif

import sys

if len(sys.argv)<2:
    print("Too few arguments")
elif len(sys.argv)>2:
    print("Too large arguments")

print("hello, my name is", sys.argv[1])

#sys.exit

import sys

if len(sys.argv)<2:
    print("Too few arguments")
elif len(sys.argv)>2:
    sys.exit("Too large arguments")
    
print("hello, my name is", sys.argv[1])

#if, for

import sys

if len(sys.argv)<2:
    sys.exit("Too few arguments")

for arg in sys.argv:
    print("hello, my name is", arg)

#slice

import sys

if len(sys.argv)<2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:-1]:
    print("hello, my name is", arg)
