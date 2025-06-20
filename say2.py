#under saying.py

#hello
import sys

from saying import hello
if len(sys.argv) == 2:
    hello(sys.argv[1])

#goodbye
import sys

from saying import goodbye
if len(sys.argv) == 2:
    goodbye(sys.argv[1])