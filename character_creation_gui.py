import tkinter as tk

def get_name():
    user_name = name_entry.get()
    print(f"Name entered: {user_name}")

root = tk.Tk()
root.title("My D&D Character Generator")

name_label = tk.Label(root, text="Character Name:")
name_label.pack(anchor="w")

name_entry = tk.Entry(root)
name_entry.pack(anchor="w")

test_button = tk.Button(root, text="Test Name", command=get_name)
test_button.pack()

root.mainloop()