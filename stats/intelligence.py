#intelligence
from .roll_stat_dice import roll_4d6_drop_lowest

def roll_intelligence():
    intelligence = roll_4d6_drop_lowest()
    return intelligence

def get_intelligence_modifier(intelligence):
    return (intelligence - 10) // 2