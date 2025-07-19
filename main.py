import json
from stats.strength import roll_strength, get_strength_modifier
from stats.dexterity import roll_dexterity, get_dexterity_modifier, calculate_unarmored_ac
from stats.constitution import roll_constitution, get_constitution_modifier, calculate_health
from stats.intelligence import roll_intelligence, get_intelligence_modifier
from stats.wisdom import roll_wisdom, get_wisdom_modifier
from stats.charisma import roll_charisma, get_charisma_modifier
from stats.classes import CLASSES

def save_character_to_json(character_data, filename):
    with open(filename, 'w') as f:
        json.dump(character_data, f, indent=2)

def load_character_from_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)
    
def create_character():
    strength = roll_strength()
    dexterity = roll_dexterity()
    constitution = roll_constitution()
    intelligence = roll_intelligence()
    wisdom = roll_wisdom()
    charisma = roll_charisma()
    
    name = input("Enter Character name: ")
    print("Available classes:", list(CLASSES.keys()))
    character_class = input("Enter Character class: ")
    
    character = {
        "name": name,
        "class": character_class,
        "stats": {
            "strength": {"score": strength, "modifier": get_strength_modifier(strength)},
            "dexterity": {"score": dexterity, "modifier": get_dexterity_modifier(dexterity)},
            "constitution": {"score": constitution, "modifier": get_constitution_modifier(constitution)},
            "intelligence": {"score": intelligence, "modifier": get_intelligence_modifier(intelligence)},
            "wisdom": {"score": wisdom, "modifier": get_wisdom_modifier(wisdom)},
            "charisma": {"score": charisma, "modifier": get_charisma_modifier(charisma)},
            "health": calculate_health(character_class, get_constitution_modifier(constitution)),
            "unarmored ac": calculate_unarmored_ac(get_dexterity_modifier(dexterity)),
        }
    }
    return character

if __name__ == "__main__":
    test_character = create_character()
    print(f"Created character: {test_character}")
    
    # Create unique filename based on character name
    filename = f"{test_character['name'].replace(' ', '_').lower()}_character.json"
    save_character_to_json(test_character, filename)
    print(f"Character saved to {filename}!")