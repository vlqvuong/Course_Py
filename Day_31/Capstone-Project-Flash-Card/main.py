from tkinter import *

import pandas
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
data_dict = {}
word_picked ={}
# Create Flash Card:

try:
    dataframe = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("./data/English-Vietnamese.csv")
    data_dict = original_data.to_dict(orient="record")
else:
    data_dict = dataframe.to_dict(orient="record")


def learn_word():
    global word_picked, flip_timer
    window.after_cancel(flip_timer)
    word_picked = random.choice(data_dict)
    canvas.itemconfig(title_text, text="English", fill="black")
    canvas.itemconfig(word_text, text=word_picked["English"], fill="black")
    canvas.itemconfig(card, image=card_front_image)
    flip_timer = window.after(3000, func=mean_word)


def mean_word():
    canvas.itemconfig(card, image=card_back_image)
    canvas.itemconfig(title_text, text="Vietnamese", fill="white")
    canvas.itemconfig(word_text, text=word_picked["Vietnamese"], fill="white")


def is_known():
    data_dict.remove(word_picked)
    data = pandas.DataFrame(data_dict)
    data.to_csv("./data/words_to_learn.csv", index=False)
    learn_word()


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card = canvas.create_image(400, 263, image=card_front_image)
title_text = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
card_back_image = PhotoImage(file="images/card_back.png")


right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=learn_word)
wrong_button.grid(column=0, row=1)

learn_word()
flip_timer = window.after(3000, func=mean_word)


window.mainloop()
