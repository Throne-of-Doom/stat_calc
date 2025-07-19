#dexterity
from .roll_stat_dice import roll_4d6_drop_lowest

def roll_dexterity():
    dexterity = roll_4d6_drop_lowest()
    return dexterity

def get_dexterity_modifier(dexterity):
    return (dexterity - 10) // 2

def calculate_unarmored_ac(dexterity_modifier):
    return 10 + dexterity_modifier