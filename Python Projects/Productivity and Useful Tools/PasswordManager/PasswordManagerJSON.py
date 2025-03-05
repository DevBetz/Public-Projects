# imports
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Constant Variables:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '?', '@', '^', '_', '=', '{', '}', '[', ']', '<','>', '.', '~', '/']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(3, 5)
nr_numbers = random.randint(5, 8)


def GeneratePassword():
    password_list = []
    # turn password back into a string
    for char in range(1, nr_letters + 1):
       password_list.append(random.choice(letters))

    for char in range(1, nr_symbols + 1):
       password_list += random.choice(symbols)

    for char in range(1, nr_numbers + 1):
      password_list += random.choice(numbers)

    # shuffle order
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(END, string=f"{password}")
    # copy to clipboard:
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def Add():
   website = website_entry.get()
   email = email_entry.get()
   password = password_entry.get()
   new_data = {website: {"email": email, "password": password}}
   
   if len(website) == 0 or len(password) == 0:
       messagebox.showinfo(title="Error!", message="Please make sure all fields are filled out")
   else:
       # Try opening the JSON file and update it
       try:
           with open("data.json", "r") as data_file:
               # If the file exists and has data, load it
               data = json.load(data_file)
       except (FileNotFoundError, json.JSONDecodeError):
           # If the file doesn't exist or is empty, start with an empty dictionary
           data = {}

       # Add new entry to the data dictionary
       data.update(new_data)

       # Write the updated data back to the file
       with open("data.json", "w") as data_file:
           json.dump(data, data_file, indent=4)

       # Clear the entry fields after adding
       website_entry.delete(0, END)
       password_entry.delete(0, END)
       messagebox.showinfo(title="Password Added", message="Your password has been successfully added!")


# ---------------------------- Search ------------------------------- #
def Search():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="File Not Found!", message=f"No data found")
    else:
        if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        elif len(website) == 0:
            messagebox.showinfo(title="Error!", message="Please make sure all required fields are filled out")
        else:
            messagebox.showinfo(title="Entry Not Found!", message=f"No entry fonud for {website}")
        



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=15, pady=15)

canvas = Canvas(height=400, width=400)

# Logo Display
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

# Search Button:
Search_Button = Button(text="Search", command=Search)
Search_Button.grid(column=2, row=1)

# Text Box 1 for website
website_entry = Entry(width=30)
website_entry.insert(END, string="")
website_entry.grid(column=1, row=1)

# Secondary Text box for email input:
email_entry = Entry(width=30)
email_entry.insert(END, string="email@example.com")
email_entry.grid(column=1, row=2)

# Text box for password gen.
password_entry = Entry(width=30)
password_entry.insert(END, string="")
password_entry.grid(column=1, row=3)

# Labels
website_label = Label(text="Website Name:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/ Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

window.mainloop()

