import tkinter as tk
from os import system
import pyjokes
root = tk.Tk()
root.geometry("500x100")
root.title("RANDOM JOKES")
T = tk.Text(root, height=4, width=80, bg= "lightblue")
T.pack()
def genrtejoke():
    global joke
    joke = pyjokes.get_joke()
    T.insert(tk.END, joke)
b = tk.Button(text= "JOKE OF THE DAY", command = genrtejoke, bg= "red")
b.pack()
root.mainloop()