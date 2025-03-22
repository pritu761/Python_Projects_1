BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random
current_card={}
data = pandas.read_csv("data/french_words.csv")
dictionary = data.to_dict(orient="records")

def new_data():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(dictionary)
    canvas.itemconfig(title1,text="French", fill="black")
    canvas.itemconfig(keyword , text = current_card["French"], fill="black")
    canvas.itemconfig(card_background,image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)

window = Tk()
window.title("Flash Card Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

def flip_card():
    canvas.itemconfig(title1,text="English")
    canvas.itemconfig(keyword,text=current_card["English"])
    canvas.item_config(card_background, image=card_back_image)

flip_timer = window.after(3000,func = flip_card)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage("image/card_front.png")
card_back_image = PhotoImage("image/card_back.png")
card_background = canvas.create_image(400,263,image=card_front_image)
title1=canvas.create_text(400,150,text="Title",font=("Arial",40,"italic"))
keyword=canvas.create_text(400,263, text="Keyword", font=("Arial",60,))
canvas.config(bg=BACKGROUND_COLOR ,highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)




cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=2, command=new_data)
unknown_button.grid(row=1,column=0)

right_image = PhotoImage(file="images/right.png")
new_button = Button(image=right_image, highlightthickness=0, command=new_data)
new_button.grid(row=1,column=1)

new_data()

window.mainloop()


