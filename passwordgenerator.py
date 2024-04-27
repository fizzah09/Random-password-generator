import tkinter as tk
from tkinter import messagebox
import string
import random

def generate_password():
    length = int(length_entry.get())
    
    if length <= 0:
        messagebox.showerror("Error", "Password length must be greater than 0")
        return

    characterlist = ''
    if digit_var.get():
        characterlist += string.digits
    if letter_var.get():
        characterlist += string.ascii_letters
    if special_var.get():
        characterlist += string.punctuation
    
    if not characterlist:
        messagebox.showerror("Error", "Select at least one character set")
        return
    
    password = ''.join(random.choice(characterlist) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Create main window
root = tk.Tk()
root.title("Password Generator")

# Length label and entry
length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=5)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=5)

# Character set checkboxes
digit_var = tk.BooleanVar()
digit_checkbox = tk.Checkbutton(root, text="Digits (0-9)", variable=digit_var)
digit_checkbox.grid(row=1, column=0, padx=10, pady=5, sticky="w")

letter_var = tk.BooleanVar()
letter_checkbox = tk.Checkbutton(root, text="Letters (a-z, A-Z)", variable=letter_var)
letter_checkbox.grid(row=2, column=0, padx=10, pady=5, sticky="w")

special_var = tk.BooleanVar()
special_checkbox = tk.Checkbutton(root, text="Special Characters", variable=special_var)
special_checkbox.grid(row=3, column=0, padx=10, pady=5, sticky="w")

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Generated password entry
password_entry_label = tk.Label(root, text="Generated Password:")
password_entry_label.grid(row=5, column=0, padx=10, pady=5)
password_entry = tk.Entry(root)
password_entry.grid(row=5, column=1, padx=10, pady=5)

# Run the application
root.mainloop()
