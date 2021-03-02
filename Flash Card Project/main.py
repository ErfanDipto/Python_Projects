import tkinter as tk
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pd.read_csv("./data/words_to_learn.csv")
    to_learn = data.to_dict(orient="records")
except FileNotFoundError:
    data = pd.read_csv("./data/french_words.csv")
    original_data_dict = data.to_dict(orient="records")
    to_learn = original_data_dict

current_card = {}
# print(to_learn)

# function to go to next card


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=f"{current_card['French']}", fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=f"{current_card['English']}", fill="white")
    canvas.itemconfig(card_background, image=card_back_image)


def is_known():
    # global to_learn
    to_learn.remove(current_card)
    next_card()
    save = pd.DataFrame(to_learn)
    save.to_csv("./data/words_to_learn.csv", index=False)


# UI creation

# Window

window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# canvas creation

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

# card_back
card_back_image = tk.PhotoImage(file="./images/card_back.png")
# image_back = canvas.create_image(400, 263, image=card_back_image)
# canvas.grid(row=0, column=0, columnspan=2)

card_front_image = tk.PhotoImage(file="./images/card_front.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
canvas.grid(row=0, column=0, columnspan=2)

# french text
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "normal"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

# wrong button
# wr_button_canv = tk.Canvas(width=100, height=100)
wr_button_img = tk.PhotoImage(file="./images/wrong.png")
wr_button = tk.Button(image=wr_button_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
wr_button.grid(row=1, column=0)

# right button
rt_button_img = tk.PhotoImage(file="./images/right.png")
rt_button = tk.Button(image=rt_button_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=is_known)
rt_button.grid(row=1, column=1)
next_card()

window.mainloop()
