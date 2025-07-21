# D&D Character Generator

This is personal project 1 of Chris Gray for Boot.dev.

## Description
This project is a D&D 5e Character Generator built with Python and tkinter. Its purpose is to generate basic characters and handle core stat generation with a user-friendly GUI.

## Features
- Supports all basic D&D 5e races and classes
- Special support for Variant Human and Half-Elf racial stat selection
- Automatically generates all six ability scores (Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma)
- Calculates ability modifiers, health, and unarmored AC
- Uses 4d6 drop lowest for stat generation
- Individual stat reroll functionality
- Saves characters to JSON files

## Current Limitations
The system does not currently support:
- Feats
- Skills
- Proficiencies  
- Inventory

## How to Run

1. Clone the repository:
git clone https://github.com/Throne-of-Doom/stat_calc

2. Navigate to project directory

cd stat_calc

3. Run the Program

python character_creation_gui.py