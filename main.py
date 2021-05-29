from tkinter import *
import pandas
import random

pair = {}

def timer():
    english = pair["English"]
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=english, fill="white")


def gen_new_word():
    global flip_timer
    global pair


    window.after_cancel(flip_timer)
    pair = random.choice(data_list)
    french = pair["French"]

    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=french, fill="black")
    flip_timer = window.after(3000, timer)


def guessed():
    data_list.remove(pair)
    gen_new_word()

def not_guessed():
    gen_new_word()


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas()
canvas.config(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
# bg_img = PhotoImage(file="images/card_front.gif")
# canvas.create_image(400, 270, image=bg_img)

title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 283, text="Word", font=("Ariel", 60, "italic"))

right = Button(text="✅", font=("Ariel", 40, "italic"), command=guessed)
right.grid(row=1, column=0)
wrong = Button(text="❌", font=("Ariel", 40, "bold"), command=not_guessed)
wrong.grid(row=1, column=1)

try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("french_words.csv")

data_list = data.to_dict(orient="records")
print(data_list)

flip_timer = window.after(3000, timer)
gen_new_word()

window.mainloop()
data_frame = pandas.DataFrame(data_list)
data_frame.to_csv("words_to_learn.csv", index=False)
