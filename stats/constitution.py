#constitution
from .roll_stat_dice import roll_4d6_drop_lowest
from .classes import CLASSES

def roll_constitution():
    constitution = roll_4d6_drop_lowest()
    return constitution

def get_constitution_modifier(constitution):
    return (constitution - 10) // 2

def calculate_health(character_class, constitution_modifier):
    hit_die = CLASSES[character_class]
    return hit_die + constitution_modifier