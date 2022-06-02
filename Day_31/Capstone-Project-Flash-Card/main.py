from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
data_dict = {}
word_picked = {}
# Create Flash Card:

try:
    dataframe = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("./data/3000_words_English.csv")
    data_dict = original_data.to_dict(orient="record")
else:
    data_dict = dataframe.to_dict(orient="record")


def learn_word():
    global word_picked, flip_timer
    window.after_cancel(flip_timer)
    word_picked = random.choice(data_dict)
    canvas.itemconfig(title_text, text="English", fill="black")
    canvas.itemconfig(ipa_text, text=word_picked["IPA"], fill="black")
    canvas.itemconfig(learn_text, text=word_picked["English"], fill="black")
    canvas.itemconfig(card, image=card_front_image)
    flip_timer = window.after(3000, func=mean_word)


def mean_word():
    canvas.itemconfig(card, image=card_back_image)
    canvas.itemconfig(title_text, text="Vietnamese", fill="white")
    canvas.itemconfig(learn_text, text=word_picked["Vietnamese"], fill="white")


def is_known():
    data_dict.remove(word_picked)
    data = pd.DataFrame(data_dict)
    data.to_csv("./data/words_to_learn.csv", index=False)
    learn_word()


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=mean_word)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card = canvas.create_image(400, 263, image=card_front_image)
title_text = canvas.create_text(400, 150, text="", font=("Arial", 20, "italic"))
ipa_text = canvas.create_text(400, 225, text="", font=("Arial", 20, "italic"))
learn_text = canvas.create_text(400, 300, text="", font=("Arial", 30, "bold"))
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


window.mainloop()
