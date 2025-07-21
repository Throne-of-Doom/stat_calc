"""
D&D Character Creation System

This module provides core functionality for creating D&D characters with
random ability scores, class and race selection, and character persistence.
Supports both command-line and GUI character creation workflows.
"""

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
    """
    Save character data to a JSON file.
    
    Args:
        character_data (dict): Complete character information dictionary
        filename (str): Name of the file to save to
    """
    with open(filename, 'w') as f:
        json.dump(character_data, f, indent=2)

def load_character_from_json(filename):
    """
    Load character data from a JSON file.
    
    Args:
        filename (str): Name of the file to load from
        
    Returns:
        dict: Character data dictionary
    """
    with open(filename, 'r') as f:
        return json.load(f)
    
def create_character():
    """
    Create a D&D character through command-line interface.
    
    Prompts user for character name, class, and race selections.
    Handles racial stat bonuses including customizable choice bonuses.
    Rolls random ability scores and applies all modifiers.
    
    Returns:
        dict: Complete character data structure
    """
    # Roll base ability scores (3d6 for each)
    strength = roll_strength()
    dexterity = roll_dexterity()
    constitution = roll_constitution()
    intelligence = roll_intelligence()
    wisdom = roll_wisdom()
    charisma = roll_charisma()
    
    # Get character name from user
    name = input("Enter Character name: ")
    
    # Class selection with validation
    while True:
        print("Available classes:", list(CLASSES.keys()))
        character_class = input("Choose your class: ")
        if character_class in CLASSES:
            break
        else:
            print("Invalid class, please try again.")
    
    # Race selection with validation and racial bonuses
    while True:
        print("Available races:", list(RACES.keys()))
        character_race = input("Choose your race: ")
        if character_race in RACES:
            # Apply fixed racial bonuses to all stats
            strength += RACES[character_race]["strength"]
            dexterity += RACES[character_race]["dexterity"]
            constitution += RACES[character_race]["constitution"]
            intelligence += RACES[character_race]["intelligence"]
            wisdom += RACES[character_race]["wisdom"]
            charisma += RACES[character_race]["charisma"]
            
            # Handle customizable racial stat bonuses
            racial_stat_bonus1 = None
            racial_stat_bonus2 = None
            
            while True:
                # Exit if race doesn't have choice bonuses
                if "choice" not in RACES[character_race]:
                    break
                
                # Handle first choice bonus
                if "choice" in RACES[character_race] and racial_stat_bonus1 is None:
                    available_stats = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
                    print("Available Stats:", available_stats)
                    racial_stat_bonus1 = input("Choose first bonus stat: ")
                    if racial_stat_bonus1 in available_stats:
                        # Apply the bonus to the selected stat
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
                
                # Handle second choice bonus
                if "choice" in RACES[character_race] and racial_stat_bonus1 is not None and racial_stat_bonus2 is None:
                    available_stats = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
                    # Remove first choice to prevent duplicates
                    if racial_stat_bonus1 in available_stats:
                        available_stats.remove(racial_stat_bonus1)
                        print("Available Stats:", available_stats)
                        racial_stat_bonus2 = input("Choose second bonus stat: ")
                        if racial_stat_bonus2 in available_stats:
                            # Apply the bonus to the selected stat and exit
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
    
    # Create complete character data structure
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


def create_character_from_gui(name, character_class, character_race, racial_choice1=None, racial_choice2=None):
    """
    Create a D&D character from GUI-provided parameters.
    
    Similar to create_character() but takes all parameters directly instead of
    prompting for user input. Handles racial choice bonuses more streamlining
    by tracking total racial bonuses separately.
    
    Args:
        name (str): Character name
        character_class (str): Selected character class
        character_race (str): Selected character race
        racial_choice1 (str, optional): First choice racial stat bonus
        racial_choice2 (str, optional): Second choice racial stat bonus
        
    Returns:
        dict: Complete character data structure
    """
    # Roll base ability scores (3d6 for each)
    strength = roll_strength()
    dexterity = roll_dexterity()
    constitution = roll_constitution()
    intelligence = roll_intelligence()
    wisdom = roll_wisdom()
    charisma = roll_charisma()

    # Apply base racial bonuses to all stats
    strength += RACES[character_race]["strength"]
    dexterity += RACES[character_race]["dexterity"]
    constitution += RACES[character_race]["constitution"]
    intelligence += RACES[character_race]["intelligence"]
    wisdom += RACES[character_race]["wisdom"]
    charisma += RACES[character_race]["charisma"]
    
    # Track total racial bonuses including choice bonuses for display
    total_str_racial = RACES[character_race]["strength"]
    total_dex_racial = RACES[character_race]["dexterity"]
    total_con_racial = RACES[character_race]["constitution"]
    total_int_racial = RACES[character_race]["intelligence"]
    total_wis_racial = RACES[character_race]["wisdom"]
    total_cha_racial = RACES[character_race]["charisma"]
    
    # Apply first choice bonus if provided and race supports choices
    if racial_choice1 and "choice" in RACES[character_race]:
        if racial_choice1 == "strength":
            strength += RACES[character_race]["choice bonus"]
            total_str_racial += RACES[character_race]["choice bonus"]
        elif racial_choice1 == "dexterity":
            dexterity += RACES[character_race]["choice bonus"]
            total_dex_racial += RACES[character_race]["choice bonus"]
        elif racial_choice1 == "constitution":
            constitution += RACES[character_race]["choice bonus"]
            total_con_racial += RACES[character_race]["choice bonus"]
        elif racial_choice1 == "intelligence":
            intelligence += RACES[character_race]["choice bonus"]
            total_int_racial += RACES[character_race]["choice bonus"]
        elif racial_choice1 == "wisdom":
            wisdom += RACES[character_race]["choice bonus"]
            total_wis_racial += RACES[character_race]["choice bonus"]
        elif racial_choice1 == "charisma":
            charisma += RACES[character_race]["choice bonus"]
            total_cha_racial += RACES[character_race]["choice bonus"]
    
    # Apply second choice bonus if provided and race supports choices
    if racial_choice2 and "choice" in RACES[character_race]:
        if racial_choice2 == "strength":
            strength += RACES[character_race]["choice bonus"]
            total_str_racial += RACES[character_race]["choice bonus"]
        elif racial_choice2 == "dexterity":
            dexterity += RACES[character_race]["choice bonus"]
            total_dex_racial += RACES[character_race]["choice bonus"]
        elif racial_choice2 == "constitution":
            constitution += RACES[character_race]["choice bonus"]
            total_con_racial += RACES[character_race]["choice bonus"]
        elif racial_choice2 == "intelligence":
            intelligence += RACES[character_race]["choice bonus"]
            total_int_racial += RACES[character_race]["choice bonus"]
        elif racial_choice2 == "wisdom":
            wisdom += RACES[character_race]["choice bonus"]
            total_wis_racial += RACES[character_race]["choice bonus"]
        elif racial_choice2 == "charisma":
            charisma += RACES[character_race]["choice bonus"]
            total_cha_racial += RACES[character_race]["choice bonus"]

    # Create complete character data structure with total racial bonuses
    character = {
        "name": name,
        "class": character_class,
        "race": character_race,
        "stats": {
            "strength": {"score": strength, "racial bonus": total_str_racial, "modifier": get_strength_modifier(strength)},
            "dexterity": {"score": dexterity, "racial bonus": total_dex_racial, "modifier": get_dexterity_modifier(dexterity)},
            "constitution": {"score": constitution, "racial bonus": total_con_racial, "modifier": get_constitution_modifier(constitution)},
            "intelligence": {"score": intelligence, "racial bonus": total_int_racial, "modifier": get_intelligence_modifier(intelligence)},
            "wisdom": {"score": wisdom, "racial bonus": total_wis_racial, "modifier":  get_wisdom_modifier(wisdom)},
            "charisma": {"score": charisma, "racial bonus": total_cha_racial, "modifier": get_charisma_modifier(charisma)},
            "health": calculate_health(character_class, get_constitution_modifier(constitution)),
            "unarmored ac": calculate_unarmored_ac(get_dexterity_modifier(dexterity)),
        }
    }
    return character

# Main execution block - runs only when script is executed directly
if __name__ == "__main__":
    # Create a test character using command-line interface
    test_character = create_character()
    print(f"Created character: {test_character}")
    
    # Create unique filename based on character name (sanitized for filesystem)
    filename = f"{test_character['name'].replace(' ', '_').lower()}_character.json"
    save_character_to_json(test_character, filename)
    print(f"Character saved to {filename}!")