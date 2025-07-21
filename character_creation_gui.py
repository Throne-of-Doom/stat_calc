"""
D&D Character Creation GUI

This module provides a graphical user interface for creating D&D characters
with customizable stats, classes, and races. Users can generate characters,
reroll individual stats, and save characters to JSON files.
"""

import tkinter as tk
from tkinter import ttk
from stats.classes import CLASSES
from stats.races import RACES
from main import create_character_from_gui, save_character_to_json
from stats.constitution import calculate_health, get_constitution_modifier

def generate_character():
    """
    Generate a complete D&D character based on GUI input values.
    
    Retrieves values from GUI elements, creates a character using the main
    character creation function, and updates all display fields with the
    generated character's information. Also saves the character to a JSON file.
    """
    # Get input values from GUI elements
    name = name_entry.get()
    character_class = class_dropdown.get()
    character_race = race_dropdown.get()

    # Get optional racial stat choices (None if not selected)
    racial_choice1 = choice1_dropdown.get() if choice1_dropdown.get() else None
    racial_choice2 = choice2_dropdown.get() if choice2_dropdown.get() else None
    
    # Create character using main creation function
    character = create_character_from_gui(name, character_class, character_race, racial_choice1, racial_choice2)
    
    # Update all display fields with character information
    name_display.delete(0, tk.END)
    name_display.insert(0, f"Name: {character['name']}")
    
    class_display.delete(0, tk.END)
    class_display.insert(0, f"Class: {character['class']}")
    
    race_display.delete(0, tk.END)
    race_display.insert(0, f"Race: {character['race']}")
    
    health_display.delete(0, tk.END)
    health_display.insert(0, f"Max Health: {character['stats']['health']}")
    
    unarmored_ac_display.delete(0, tk.END)
    unarmored_ac_display.insert(0, f"Unarmored AC: {character['stats']['unarmored ac']}")
    
    # Update all six ability score displays with score, modifier, and racial bonus
    strength_display.delete(0, tk.END)
    strength_display.insert(0, f"Strength: {character['stats']['strength']['score']} ({character['stats']['strength']['modifier']:+d}) (Racial: +{character['stats']['strength']['racial bonus']})")
    
    dexterity_display.delete(0, tk.END)
    dexterity_display.insert(0, f"Dexterity: {character['stats']['dexterity']['score']} ({character['stats']['dexterity']['modifier']:+d}) (Racial: +{character['stats']['dexterity']['racial bonus']})")
    
    constitution_display.delete(0, tk.END)
    constitution_display.insert(0, f"Constitution: {character['stats']['constitution']['score']} ({character['stats']['constitution']['modifier']:+d}) (Racial: +{character['stats']['constitution']['racial bonus']})")
    
    intelligence_display.delete(0, tk.END)
    intelligence_display.insert(0, f"Intelligence: {character['stats']['intelligence']['score']} ({character['stats']['intelligence']['modifier']:+d}) (Racial: +{character['stats']['intelligence']['racial bonus']})")
    
    wisdom_display.delete(0, tk.END)
    wisdom_display.insert(0, f"Wisdom: {character['stats']['wisdom']['score']} ({character['stats']['wisdom']['modifier']:+d}) (Racial: +{character['stats']['wisdom']['racial bonus']})")
    
    charisma_display.delete(0, tk.END)
    charisma_display.insert(0, f"Charisma: {character['stats']['charisma']['score']} ({character['stats']['charisma']['modifier']:+d}) (Racial: +{character['stats']['charisma']['racial bonus']})")

    # Save character to JSON file with sanitized filename
    filename = f"{character['name'].replace(' ', '_').lower()}_character.json"
    save_character_to_json(character, filename)
    print(f"Character saved to {filename}!")

def on_race_change(event):
    """
    Handle race dropdown selection changes.
    
    Shows or hides the racial stat choice dropdowns based on whether
    the selected race has customizable stat bonuses.
    
    Args:
        event: Tkinter event object (not used but required by callback)
    """
    selected_race = race_dropdown.get()
    
    # Check if the selected race has choice bonuses
    if "choice" in RACES.get(selected_race, {}):
        # Show the choice dropdowns for races with customizable bonuses
        choice1_label.pack(anchor="w")
        choice1_dropdown.pack(anchor="w")
        choice2_label.pack(anchor="w")
        choice2_dropdown.pack(anchor="w")
    else:
        # Hide the choice dropdowns for races with fixed bonuses
        choice1_label.pack_forget()
        choice1_dropdown.pack_forget()
        choice2_label.pack_forget()
        choice2_dropdown.pack_forget()

def on_first_choice_change(event):
    """
    Handle first racial stat choice dropdown changes.
    
    Updates the second choice dropdown to exclude the already-selected stat,
    preventing duplicate selections.
    
    Args:
        event: Tkinter event object (not used but required by callback)
    """
    first_choice = choice1_dropdown.get()
    
    # Get all available ability scores
    all_stats = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
    
    # Remove the first choice from the second dropdown's options
    if first_choice in all_stats:
        remaining_stats = [stat for stat in all_stats if stat != first_choice]
        choice2_dropdown.config(values=remaining_stats)
        
        # Clear the second dropdown if it has the same value as first choice
        if choice2_dropdown.get() == first_choice:
            choice2_dropdown.set("")

def reroll_single_stat(stat_name):
    """
    Reroll a single ability score for the current character.
    
    Generates a new character with the same configuration but fresh dice rolls,
    then updates only the specified stat display. Also updates dependent stats
    (health for constitution, AC for dexterity).
    
    Args:
        stat_name (str): Name of the stat to reroll ('strength', 'dexterity', etc.)
    """
    # Get current selections from GUI
    name = name_entry.get()
    character_class = class_dropdown.get()
    character_race = race_dropdown.get()
    racial_choice1 = choice1_dropdown.get() if choice1_dropdown.get() else None
    racial_choice2 = choice2_dropdown.get() if choice2_dropdown.get() else None
    
    # Only proceed if we have all required information
    if name and character_class and character_race:
        # Generate a new character to get fresh stat rolls
        character = create_character_from_gui(name, character_class, character_race, racial_choice1, racial_choice2)
        
        # Update only the specific stat display based on stat_name
        if stat_name == 'strength':
            strength_display.delete(0, tk.END)
            strength_display.insert(0, f"Strength: {character['stats']['strength']['score']} ({character['stats']['strength']['modifier']:+d}) (Racial: +{character['stats']['strength']['racial bonus']})")
        elif stat_name == 'dexterity':
            dexterity_display.delete(0, tk.END)
            dexterity_display.insert(0, f"Dexterity: {character['stats']['dexterity']['score']} ({character['stats']['dexterity']['modifier']:+d}) (Racial: +{character['stats']['dexterity']['racial bonus']})")
            # Update unarmored AC since it depends on dexterity modifier
            unarmored_ac_display.delete(0, tk.END)
            unarmored_ac_display.insert(0, f"Unarmored AC: {character['stats']['unarmored ac']}")
        elif stat_name == 'constitution':
            constitution_display.delete(0, tk.END)
            constitution_display.insert(0, f"Constitution: {character['stats']['constitution']['score']} ({character['stats']['constitution']['modifier']:+d}) (Racial: +{character['stats']['constitution']['racial bonus']})")
            # Update health since it depends on constitution modifier
            health_display.delete(0, tk.END)
            health_display.insert(0, f"Max Health: {character['stats']['health']}")
        elif stat_name == 'intelligence':
            intelligence_display.delete(0, tk.END)
            intelligence_display.insert(0, f"Intelligence: {character['stats']['intelligence']['score']} ({character['stats']['intelligence']['modifier']:+d}) (Racial: +{character['stats']['intelligence']['racial bonus']})")
        elif stat_name == 'wisdom':
            wisdom_display.delete(0, tk.END)
            wisdom_display.insert(0, f"Wisdom: {character['stats']['wisdom']['score']} ({character['stats']['wisdom']['modifier']:+d}) (Racial: +{character['stats']['wisdom']['racial bonus']})")
        elif stat_name == 'charisma':
            charisma_display.delete(0, tk.END)
            charisma_display.insert(0, f"Charisma: {character['stats']['charisma']['score']} ({character['stats']['charisma']['modifier']:+d}) (Racial: +{character['stats']['charisma']['racial bonus']})")

# Initialize main window
root = tk.Tk()
root.title("My D&D Character Generator")

# Character name input section
name_label = tk.Label(root, text="Character Name:")
name_label.pack(anchor="w")

name_entry = tk.Entry(root)
name_entry.pack(anchor="w")

# Class selection section
class_label = tk.Label(root, text="Class:")
class_label.pack(anchor="w")

class_dropdown = ttk.Combobox(root, values=list(CLASSES.keys()))
class_dropdown.pack(anchor="w")

# Race selection section
race_label = tk.Label(root, text="Race:")
race_label.pack(anchor="w")

race_dropdown = ttk.Combobox(root, values=list(RACES.keys()))
race_dropdown.pack(anchor="w")
race_dropdown.bind("<<ComboboxSelected>>", on_race_change)

# Racial stat choice sections (initially visible, then hidden)
# These are shown/hidden based on selected race's capabilities
choice1_label = tk.Label(root, text="First Bonus Stat:")
choice1_label.pack(anchor="w")

choice1_dropdown = ttk.Combobox(root, values=["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"])
choice1_dropdown.pack(anchor="w")
choice1_dropdown.bind("<<ComboboxSelected>>", on_first_choice_change)

choice2_label = tk.Label(root, text="Second Bonus Stat:")
choice2_label.pack(anchor="w")

choice2_dropdown = ttk.Combobox(root, values=["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"])
choice2_dropdown.pack(anchor="w")

# Hide choice elements initially (shown only for applicable races)
choice1_label.pack_forget()
choice1_dropdown.pack_forget()
choice2_label.pack_forget()
choice2_dropdown.pack_forget()

# Character information display fields
# These show the generated character's stats and info
name_display = tk.Entry(root, width=30)
name_display.pack(anchor="e")

class_display = tk.Entry(root, width=30)
class_display.pack(anchor="e")

race_display = tk.Entry(root, width=30)
race_display.pack(anchor="e")

health_display = tk.Entry(root, width=30)
health_display.pack(anchor="e")

unarmored_ac_display = tk.Entry(root, width=30)
unarmored_ac_display.pack(anchor="e")

# Ability score displays with individual reroll buttons
# Each stat has a display field and a reroll button for fine-tuning
strength_display = tk.Entry(root, width=30)
strength_display.pack(anchor="e")
strength_reroll = tk.Button(root, text="Reroll Strength", command=lambda: reroll_single_stat('strength'))
strength_reroll.pack(anchor="e")

dexterity_display = tk.Entry(root, width=30)
dexterity_display.pack(anchor="e")
dexterity_reroll = tk.Button(root, text="Reroll Dexterity", command=lambda: reroll_single_stat('dexterity'))
dexterity_reroll.pack(anchor="e")

constitution_display = tk.Entry(root, width=30)
constitution_display.pack(anchor="e")
constitution_reroll = tk.Button(root, text="Reroll Constitution", command=lambda: reroll_single_stat('constitution'))
constitution_reroll.pack(anchor="e")

intelligence_display = tk.Entry(root, width=30)
intelligence_display.pack(anchor="e")
intelligence_reroll = tk.Button(root, text="Reroll Intelligence", command=lambda: reroll_single_stat('intelligence'))
intelligence_reroll.pack(anchor="e")

wisdom_display = tk.Entry(root, width=30)
wisdom_display.pack(anchor="e")
wisdom_reroll = tk.Button(root, text="Reroll Wisdom", command=lambda: reroll_single_stat('wisdom'))
wisdom_reroll.pack(anchor="e")

charisma_display = tk.Entry(root, width=30)
charisma_display.pack(anchor="e")
charisma_reroll = tk.Button(root, text="Reroll Charisma", command=lambda: reroll_single_stat('charisma'))
charisma_reroll.pack(anchor="e")

# Main generate button to create a complete character
generate = tk.Button(root, text="Generate Character", command=generate_character)
generate.pack(anchor="w")

# Start the GUI event loop
root.mainloop()