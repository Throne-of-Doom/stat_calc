#constitution
from .roll_stat_dice import roll_4d6_drop_lowest

def roll_constitution():
    constitution = roll_4d6_drop_lowest()
    return constitution