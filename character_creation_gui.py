import tkinter as tk
from tkinter import ttk
from stats.classes import CLASSES
from stats.races import RACES

def get_name():
    name = name_entry.get()
    character_class = class_dropdown.get()
    character_race = race_dropdown.get()
    print(f"Name entered: {name}, Class: {character_class}, Race: {character_race}")

root = tk.Tk()
root.title("My D&D Character Generator")

name_label = tk.Label(root, text="Character Name:")
name_label.pack(anchor="w")

name_entry = tk.Entry(root)
name_entry.pack(anchor="w")

class_label = tk.Label(root, text="Class:")
class_label.pack(anchor="w")

class_dropdown = ttk.Combobox(root, values=list(CLASSES.keys()))
class_dropdown.pack(anchor="w")

race_label = tk.Label(root, text="Race:")
race_label.pack(anchor="w")

race_dropdown = ttk.Combobox(root, values=list(RACES.keys()))
race_dropdown.pack(anchor="w")

test_button = tk.Button(root, text="Test Name", command=get_name)
test_button.pack(anchor="w")

root.mainloop()