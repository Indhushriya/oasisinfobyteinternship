import random
from tkinter import *
from tkinter import ttk
import string
import pyperclip
import re

def generate_password(length, include_letters, include_numbers, include_symbols):
    characters = ""
    if include_letters:
        characters += string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        return "Please select at least one character type."

    password = "".join(random.choice(characters) for _ in range(length))
    pyperclip.copy(password)
    return password

text1 = ""  # Declare text1 as a global variable

def switch(var):
    var.set(not var.get())

window = Tk()
window.title('ENIGMA')
window.geometry("550x400")
window.configure(bg="#020d17")

for i in range(6):
    window.columnconfigure(i, weight=1)
    window.rowconfigure(i, weight=1)

style = ttk.Style()
style.configure(
    "TCheckbutton",
    font=("Helvetica", 12),
    background="#020d17",
    foreground="#d5ebfb",
)

is_on1 = BooleanVar()
is_on2 = BooleanVar()
is_on3 = BooleanVar()

heading_label = Label(
    window,
    text="Password Generator",
    font=("Helvetica", 18),
    bg="#020d17",
    fg="#d5ebfb",
)
heading_label.grid(column=0, row=0, columnspan=4, pady=10, padx=20)

length_label = Label(
    window,
    text="Password Length:",
    font=("Helvetica", 14),
    bg="#020d17",
    fg="#d5ebfb",
)
length_label.grid(column=0, row=1, sticky="W", padx=20, pady=5)

length_entry = Entry(window, width=20, font=("Helvetica", 14))
length_entry.grid(column=1, row=1, columnspan=2, pady=5)

on_button1 = ttk.Checkbutton(
    window,
    variable=is_on1,
    onvalue=True,
    offvalue=False,
    style="TCheckbutton",
    text="Include Letters (A-Z, a-z)",
)
on_button2 = ttk.Checkbutton(
    window,
    variable=is_on2,
    onvalue=True,
    offvalue=False,
    style="TCheckbutton",
    text="Include Numbers (0-9)",
)
on_button3 = ttk.Checkbutton(
    window,
    variable=is_on3,
    onvalue=True,
    offvalue=False,
    style="TCheckbutton",
    text="Include Symbols (!@#&*)",
)

on_button1.grid(column=0, row=2, sticky="W", padx=30, pady=5)
on_button2.grid(column=0, row=3, sticky="W", padx=30, pady=5)
on_button3.grid(column=0, row=4, sticky="W", padx=30, pady=5)

def generate_password_button():
    password_length = int(length_entry.get())
    include_letters = is_on1.get()
    include_numbers = is_on2.get()
    include_symbols = is_on3.get()

    password = generate_password(password_length, include_letters, include_numbers, include_symbols)

    # Update a label or display the password as needed
    result_label.config(text="Generated Password: " + password)

    # Add dashed border to the label with a specific border color
    result_label.config(bd=1, relief="solid", highlightbackground="#86c4f3")

    global text1  # Declare text1 as a global variable
    check_password_strength(password)  # Call the function to update text1
    strength_label.config(text=text1)
    strength_label.config(bd=1, relief="solid", highlightbackground="#86c4f3")

    # Adjust the column configuration to ensure the full text is displayed
    window.columnconfigure(0, weight=1)

    # Center the text in the label
    strength_label.grid(column=0, row=7, columnspan=4, pady=10)


    copy_label = Label(
        window,
        text="Copied to clipboard!",
        font=("Helvetica", 14),
        bg="#020d17",
        fg="#d5ebfb",
    )
    copy_label.grid(column=0, row=8, columnspan=4, pady=5)

def check_password_strength(password):
    global text1  # Declare text1 as a global variable
    score = 0
    
    if len(password) >= 8:              # Check for length of password  
        score += 1

    # Check for uppercase, lowercase, and digits
    if re.search(r'[A-Z]', password) and \
       re.search(r'[a-z]', password) and \
       re.search(r'\d', password):
        score += 1

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):   # Check for special characters
        score += 1

    if score == 3:
        text1=  "Super Secure - This password is extremely strong!"
    elif score == 2:
        text1 = "Moderate - Password is moderately secure."
    else:
        text1 = "Weak - Password needs improvement."
    
result_label = Label(
    window,
    text="",
    font=("Helvetica", 14),
    bg="#020d17",
    fg="#d5ebfb",
)
result_label.grid(column=0, row=6, columnspan=4, pady=10)

strength_label = Label(
    window,
    text="Password Strength:",
    font=("Helvetica", 14),
    bg="#020d17",
    fg="#d5ebfb",
)

generate_button = Button(
    window, text="Generate Password", font=("Helvetica", 14), bg="#86c4f3", fg="#020d17", command=generate_password_button
)
generate_button.grid(column=0, row=5, columnspan=2, pady=10, padx=20)

window.mainloop()
