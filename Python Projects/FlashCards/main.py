# imports and global
from tkinter import *
from tkinter import messagebox
import pandas
import json
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# using pandas to read csv:
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")

else:
    to_learn = data.to_dict(orient="records")


#functions for buttons:
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_image)
    flip_timer = window.after(5000, func=flip_card)



# flip_card function
def flip_card():
    english_title = canvas.itemconfig(card_title, text="English", fill="white")
    english_word = canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_image)


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# window/ UI
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(5000, func=flip_card)


# front/ back image
canvas = Canvas(width= 800, height=526, bg=BACKGROUND_COLOR)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2, padx=50, pady=50)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))


# right image/ button
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)
right_button.config(padx=2, pady=2)

# wrong image/ button
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)
wrong_button.config(padx=2, pady=2)


next_card()
window.mainloop()
