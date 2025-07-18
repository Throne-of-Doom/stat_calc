#dexterity
from .roll_stat_dice import roll_4d6_drop_lowest

def roll_dexterity():
    dexterity = roll_4d6_drop_lowest()
    return dexterity