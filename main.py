from tkinter import *
import tkinter
from tkinter import Canvas
import time
from text import text1

# ********************* CONSTANTS ************************* #
BLACK = "#000000"
FONT_NAME = "Bebas Neue"

# *********** GUI ************** #
window = tkinter.Tk()
window.title("Typing Speed Test")
canvas = Canvas(width=1000, height=1000, bg=BLACK, highlightthickness=0)
canvas.create_text(530, 100, text="Speed Test", fill="white", font=(FONT_NAME, 50, "bold"))
canvas.create_text(400, 500, fill="white", font=("Courier", 11, "bold"),
                   text=text1, width=800)
canvas.pack()

# *********** PROGRAM *********** #
text_list = []
entry = tkinter.Entry(width=60)
time_start = time.time()

def start():
    global time_start
    entry.place(x=165, y=850)
    time_start = time.time()
    start_button["state"] = DISABLED


def submit():
    entry.config(state="disabled")
    time_taken = time.time() - time_start
    text_entered = entry.get()
    for text in text_entered:
        text_list.append(text)
    cpm = round(len(text_list) * (60/time_taken),2)
    words_list = text_entered.split()
    wpm = round(len(words_list) * (60/time_taken),2)
    canvas.create_text(450, 30, text=f"Your cpm is {cpm} and wpm is {wpm}", fill="white", font=(FONT_NAME, 20, "bold"))


# *********** GUI *********** #

start_button = tkinter.Button(text="Start", command=start)
start_button.place(x=400, y=880)

entry_button = tkinter.Button(text="Submit", command=submit)
entry_button.place(x=465, y=880)

window.mainloop()
