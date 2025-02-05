import tkinter as Tk
from tkinter import Canvas

import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLACK = "#000000"
FONT_NAME = "Courier"
WORK_MIN = 30
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global reps
    reps =0
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=BLACK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count: int):
    """Counts down and updates the timer display dynamically."""
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start()
        marks = "✔"
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk.Tk()
window.title("Productivity Timer")
window.config(padx=100, pady=58, bg=GREEN)

# work on refreshing/ clearing after reset or start button is clicked.
#window.after(100, timer)


# Close window event handling to cancel the timer
def on_closing():
    window.after_cancel(timer)
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)

title_label = Tk.Label(text="Timer", fg="Black", bg=GREEN, font=("Courier", 35, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
img = Tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Start Button
start_button = Tk.Button(text="Start", command=start, highlightbackground="GREEN")
start_button.grid(column=0, row=2)

# Reset Button
reset_button = Tk.Button(text="Reset", command=reset, highlightbackground="GREEN")
reset_button.grid(column=2, row=2)

# Check Marks
check_marks = Tk.Label(fg="BLACK", bg=GREEN, font=("Courier", 20))
check_marks.grid(column=1, row=3)


window.mainloop()
