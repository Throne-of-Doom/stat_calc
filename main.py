import json
from stats.strength import roll_strength, get_strength_modifier
from stats.dexterity import roll_dexterity, get_dexterity_modifier, calculate_unarmored_ac
from stats.constitution import roll_constitution, get_constitution_modifier, calculate_health
from stats.intelligence import roll_intelligence, get_intelligence_modifier
from stats.wisdom import roll_wisdom, get_wisdom_modifier
from stats.charisma import roll_charisma, get_charisma_modifier
from stats.classes import CLASSES
from stats.races import RACES

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
    while True:
        print("Available classes:", list(CLASSES.keys()))
        character_class = input("Choose your class: ")
        if character_class in CLASSES:
            break
        else:
            print("Invalid class, please try again.")
    while True:
        print("Available races:", list(RACES.keys()))
        character_race = input("Choose your race: ")
        if character_race in RACES:
            # Apply racial bonuses
            strength += RACES[character_race]["strength"]
            dexterity += RACES[character_race]["dexterity"]
            constitution += RACES[character_race]["constitution"]
            intelligence += RACES[character_race]["intelligence"]
            wisdom += RACES[character_race]["wisdom"]
            charisma += RACES[character_race]["charisma"]
            racial_stat_bonus1 = None
            racial_stat_bonus2 = None
            while True:
                if "choice" not in RACES[character_race]:
                    break
                if "choice" in RACES[character_race] and racial_stat_bonus1 is None:
                    available_stats = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
                    print("Available Stats:", available_stats)
                    racial_stat_bonus1 = input("Choose first bonus stat: ")
                    if racial_stat_bonus1 in available_stats:
                        # Apply the bonus to the actual variable
                        if racial_stat_bonus1 == "strength":
                            strength += RACES[character_race]["choice bonus"]
                        elif racial_stat_bonus1 == "dexterity":
                            dexterity += RACES[character_race]["choice bonus"]
                        elif racial_stat_bonus1 == "constitution":
                            constitution += RACES[character_race]["choice bonus"]
                        elif racial_stat_bonus1 == "intelligence":
                            intelligence += RACES[character_race]["choice bonus"]
                        elif racial_stat_bonus1 == "wisdom":
                            wisdom += RACES[character_race]["choice bonus"]
                        elif racial_stat_bonus1 == "charisma":
                            charisma += RACES[character_race]["choice bonus"]
                    else:
                        print("Invalid Stat, Please try again")
                        racial_stat_bonus1 = None
                if "choice" in RACES[character_race] and racial_stat_bonus1 is not None and racial_stat_bonus2 is None:
                    available_stats = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
                    if racial_stat_bonus1 in available_stats:
                        available_stats.remove(racial_stat_bonus1)
                        print("Available Stats:", available_stats)
                        racial_stat_bonus2 = input("Choose second bonus stat: ")
                        if racial_stat_bonus2 in available_stats:
                            # Apply the bonus to the actual variable
                            if racial_stat_bonus2 == "strength":
                                strength += RACES[character_race]["choice bonus"]
                                break
                            elif racial_stat_bonus2 == "dexterity":
                                dexterity += RACES[character_race]["choice bonus"]
                                break
                            elif racial_stat_bonus2 == "constitution":
                                constitution += RACES[character_race]["choice bonus"]
                                break
                            elif racial_stat_bonus2 == "intelligence":
                                intelligence += RACES[character_race]["choice bonus"]
                                break
                            elif racial_stat_bonus2 == "wisdom":
                                wisdom += RACES[character_race]["choice bonus"]
                                break
                            elif racial_stat_bonus2 == "charisma":
                                charisma += RACES[character_race]["choice bonus"]
                                break
                        else:
                            print("Invalid Stat, Please try again")
                            racial_stat_bonus2 = None
            break   
        else:
            print("Invalid race, please try again.")
    
    # Move this outside the while loop - fix indentation
    character = {
        "name": name,
        "class": character_class,
        "race": character_race,
        "stats": {
            "strength": {"score": strength, "racial bonus": RACES[character_race]["strength"], "modifier": get_strength_modifier(strength)},
            "dexterity": {"score": dexterity, "racial bonus": RACES[character_race]["dexterity"], "modifier": get_dexterity_modifier(dexterity)},
            "constitution": {"score": constitution, "racial bonus": RACES[character_race]["constitution"], "modifier": get_constitution_modifier(constitution)},
            "intelligence": {"score": intelligence, "racial bonus": RACES[character_race]["intelligence"], "modifier": get_intelligence_modifier(intelligence)},
            "wisdom": {"score": wisdom, "racial bonus": RACES[character_race]["wisdom"], "modifier":  get_wisdom_modifier(wisdom)},
            "charisma": {"score": charisma, "racial bonus": RACES[character_race]["charisma"], "modifier": get_charisma_modifier(charisma)},
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