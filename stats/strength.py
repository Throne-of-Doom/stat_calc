#strength stats
from .roll_stat_dice import roll_4d6_drop_lowest

def roll_strength():
    strength = roll_4d6_drop_lowest()
    return strength

def get_strength_modifier(strength):
    return (strength - 10) // 2