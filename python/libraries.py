#coin
import random

coin = random.choice(["heads", "tails"])
print(coin)

#number

import random

number = random.randint(1,10)
print(number)

#shuffle

import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)

#statistics

import statistics

print(statistics.mean([100, 90]))

#sys

import sys

print("hello, my name is", sys.argv[1])
