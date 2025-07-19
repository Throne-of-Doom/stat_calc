#charisma
from .roll_stat_dice import roll_4d6_drop_lowest

def roll_charisma():
    charisma = roll_4d6_drop_lowest()
    return charisma

def get_charisma_modifier(charisma):
    return (charisma - 10) // 2