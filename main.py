from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
card = {}
data_dict = {}

try:
    data = pandas.read_csv('./data/word_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('./data/french_words.csv')
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")



def new_card():
    global card, flip_timer
    window.after_cancel(flip_timer)
    card = random.choice(data_dict)
    print(card['French'])
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=card['French'], fill='black')
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=card['English'], fill='white')
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    data_dict.remove(card)
    data = pandas.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    new_card()


window = Tk()
window.title("Flashy")
window.config(pady=100, padx=100, background=BACKGROUND_COLOR, highlightthickness=0)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(height=526, width=800)
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file='./images/card_front.png')
card_back_img = PhotoImage(file='./images/card_back.png')
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", fill='black', font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400,263, text="", fill='black', font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file='./images/wrong.png')
cross_button = Button(image=cross_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=new_card)
cross_button.grid(row=1, column=0)

tick_image = PhotoImage(file='./images/right.png')
tick_button = Button(image=tick_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=is_known)
tick_button.grid(row=1, column=1)

new_card()

window.mainloop()
