from tkinter import *
import pandas as pd
import random
repet = []
BACKGROUND_COLOR = "#B1DDC6"
try:
    df = pd.read_csv('./data/words_to_learn.csv')
except:
    df = pd.read_csv('./data/Hindi_words.csv')
print(df)
to_learn = df.to_dict(orient="records")
index = {}

def hcard():
    global index, flip_timer
    window.after_cancel(flip_timer)
    index = random.choice(to_learn)
    hword = index["Hindi"]
    canvas.itemconfig(tittle, text="Hindi", fill="black")
    canvas.itemconfig(word, text=f"{hword}", fill="black")
    canvas.itemconfig(imagee, image=f_pic)
    flip_timer = window.after(3000, ecard)


def ecard():
    global index
    eword = index["English"]
    canvas.itemconfig(imagee, image=b_pic)
    canvas.itemconfig(tittle, text="English", fill="white")
    canvas.itemconfig(word, text=f"{eword}", fill="white")
    window.after(3000, hcard)


def is_known():
    to_learn.remove(index)
    data = pd.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    hcard()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(2000, hcard)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
f_pic = PhotoImage(file="./images/card_front.png")
b_pic = PhotoImage(file="./images/card_back.png")
imagee = canvas.create_image(400, 263, image=f_pic)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(highlightthickness=0)


tittle = canvas.create_text(400, 150, text="Tittle",
                            font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))


r_image = PhotoImage(file="./images/right.png")
r_button = Button(image=r_image, highlightthickness=0, command=is_known)
r_button.grid(row=1, column=0)

w_image = PhotoImage(file="./images/wrong.png")
w_buttom = Button(image=w_image, highlightthickness=0, command=hcard)
w_buttom.grid(row=1, column=1)

window.mainloop()
