import tkinter
window = tkinter.Tk()
window.title("GUI")
window.minsize(width = 500, height = 300)

#labler
my_label = tkinter.Label(text="Label", font=("Arial", 20, "bold"))
my_label.pack()
def button_clicked():
    print("i got clicked")
    new_txt = (input.get())
    my_label.config(text=new_txt)

button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()


#input
input = tkinter.Entry(width=10)
input.pack()







window.mainloop()