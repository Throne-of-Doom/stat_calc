import json
from stats.strength import roll_strength
from stats.dexterity import roll_dexterity
from stats.constitution import roll_constitution
from stats.intelligence import roll_intelligence
from stats.wisdom import roll_wisdom
from stats.charisma import roll_charisma

def save_character_to_json(character_data, filename):
    with open(filename, 'w') as f:
        json.dump(character_data, f, indent=2)

def load_character_from_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)
    
def create_character():
    character = {
        "name": input("Enter Character name: "),
        "stats": {
            "strength": roll_strength(),
            "dexterity": roll_dexterity(),
            "constitution": roll_constitution(),
            "intelligence": roll_intelligence(),
            "wisdom": roll_wisdom(),
            "charisma": roll_charisma()
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