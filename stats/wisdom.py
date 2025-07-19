#wisdom.py
from .roll_stat_dice import roll_4d6_drop_lowest

def roll_wisdom():
    wisdom = roll_4d6_drop_lowest()
    return wisdom

def get_wisdom_modifier(wisdom):
    return (wisdom - 10) // 2