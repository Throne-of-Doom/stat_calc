import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from stats.roll_stat_dice import roll_dice, add_rolls, roll_4d6_drop_lowest

def test_roll_4d6_drop_lowest():
    result = roll_4d6_drop_lowest()
    assert isinstance(result, int)
    assert 3 <= result <= 18

    for _ in range(10):
        result = roll_4d6_drop_lowest()
        assert 3 <= result <= 18

def test_add_rolls():
    test_rolls = [1, 2, 3, 4]
    result = add_rolls(test_rolls)
    assert result == 10

def test_roll_dice():
    for _ in range(10):
        result = roll_dice(6)
        assert 1 <= result <=6