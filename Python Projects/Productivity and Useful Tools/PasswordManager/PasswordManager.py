#imports
from tkinter import *
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Constant Vairables:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '?', '@', '^', '_', '=', '{', '}', '[', ']', '<','>', '.', '~', '/']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(3, 5)
nr_numbers = random.randint(5, 8)


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
    random.shuffle(password_list)
    password = ""
    for char in password_list:
      password += char
    password_entry.delete(0, END)
    password_entry.insert(END, string=f"{password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def Add():
  f = open("PasswordManagerList.txt", "a")
  f.write(f"\n{website_entry.get()} | {email_entry.get()} | {password_entry.get()}")
  f.close()

#open and (edited out reading the file after the appending):
  f = open("PasswordManagerList.txt", "r")
#  print(f.read())


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
Gen_Pass = Button(text="Generate Password", command=GeneratePassword)
Gen_Pass.grid(column=2, row=3)

# Button 2
Add_Button = Button(text="Add", command=Add)
Add_Button.grid(column=1, row=6)
Add_Button.config(padx=5, pady=2)

# Text Box 1 for website
website_entry = Entry(width=30)
website_entry.insert(END, string="")
website_entry.grid(column=1, row=1)

# Secondary Text box for email input:
email_entry = Entry(width=30)
email_entry.insert(END, string="email@example.com")
email_entry.grid(column=1, row=2)

# 3 Text box for password gen.
password_entry = Entry(width=30)
password_entry.insert(END, string="")
password_entry.grid(column=1, row=3)


# labels
# Website:
website_label = Label(text="Website Name:")
website_label.grid(column=0, row=1)

# Email/ Username:
email_label = Label(text="Email/ Username:")
email_label.grid(column=0, row=2)

# Password:
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)


window.mainloop()
