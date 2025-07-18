import random

def roll_dice(size):
    return random.randint(1, size)

def add_rolls(rolls):
    return sum(rolls)


def roll_4d6_drop_lowest(size=6):
    rolls = []
    for i in range(4):
        rolls.append(roll_dice(size))
    rolls.sort()
    del rolls[0]
    return add_rolls(rolls)