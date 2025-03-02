from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#imports
import random

# Constant Vairables:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '?', '@', '^', '_', '=', '{', '}', '[', ']', '<','>', '.', '~', '/']

nr_letters = 10
nr_symbols = 5
nr_numbers = 5

# not sure if i need this next line. check later.
# password = ""

def GeneratePassword():

    password_list = []
    #turn password back into a string
    for char in range(1, nr_letters + 1):
       password_list.append(random.choice(letters))

    for char in range(1, nr_symbols + 1):
       password_list += random.choice(symbols)

    for char in range(1, nr_numbers + 1):
      password_list += random.choice(numbers)
    #shuffle order
    print(password_list)
    random.shuffle(password_list)
    print(password_list)

    password = ""
    for char in password_list:
      password += char

    print(f"Your password is: {password}")
    #have it display in text box 3 --> generated password

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=15, pady=15)

canvas = Canvas(height=400, width=400)


#Logo Display
logo_img = PhotoImage(file="logo.png")
canvas.create_image(200, 200, image=logo_img)

canvas.grid(column=1, row=0)

# Buttons for alignment, change later:
# Button 1
one_button = Button(text="Generate Password")
one_button.grid(column=2, row=3)

# Button 2
two_button = Button(text="Add")
two_button.grid(column=1, row=6)
two_button.config(padx=5, pady=2)

# Text Box 1 for website
entry = Entry(width=30)
entry.insert(END, string="Website Name")

print(entry.get())
entry.grid(column=1, row=1)

# Secondary Text box for email input:
entry = Entry(width=30)
entry.insert(END, string="Email/Username")

print(entry.get())
entry.grid(column=1, row=2)

# 3 Text box for password gen.
entry = Entry(width=30)
entry.insert(END, string="Generated Password")

print(entry.get())
entry.grid(column=1, row=3)


# Website:
label = Label(text="Website:")
label.grid(column=0, row=1)

# Email/ Username:
label = Label(text="Email/ Username:")
label.grid(column=0, row=2)

# Password:
label = Label(text="Password:")
label.grid(column=0, row=3)


window.mainloop()