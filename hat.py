import random

class Hat:
    houses=["gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

Hat.sort("Harry")

#remove hat

import random

houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

def sort(name):
    print(name, "is in", random.choice(houses))

sort("Harry")