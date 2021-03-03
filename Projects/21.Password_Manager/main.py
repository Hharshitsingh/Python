from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gerate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters)for _ in range(randint(8, 10))]
    password_symbomls = [choice(symbols)for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers)for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbomls + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = website_entry.get()
    mail = email_entry.get()
    paswd = password_entry.get()
    new_data = {
        web: {
            "email": mail,
            "password": paswd
        }
    }
    if len(web) == 0 or len(paswd) == 0 or len(mail) == 0:
        messagebox.showinfo(title="OOps", message="Fill the all filds")
    else:
        # is_ok = messagebox.askokcancel(title=web, message=f"These are details entered: \nEmail: {mail}\nPassword: {paswd} \n Is it ok to save?")
        # if is_ok == True:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    web = website_entry.get()
    try:
        with open("./data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if web in data:
            email = data[web]["email"]
            password = data[web]["password"]
            messagebox.showinfo(
                title=web, message=f"Email/UserId: {email} \nPassword: {password} ")
            # print(data)
        else:
            messagebox.showinfo(title="Error", message=f"No Datail of {web}")
        website_entry.delete(0, END)
        


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("PassWord Manager")
window.config(padx=50, pady=50)
window.iconbitmap("./icon.ico")

canvas = Canvas(width=200, height=200)
pic = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=pic)
canvas.grid(column=1, row=0)

website = Label(text="Website:")
website.grid(column=0, row=1)
website_entry = Entry(width=39)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)
search = Button(text="Search", command=search)
search.grid(column=2, row=1)

email = Label(text="Email/Username:")
email.grid(column=0, row=2)
email_entry = Entry(width=39)
email_entry.insert(0, "xyz@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

password = Label(text="Password:")
password.grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_password = Button(text="Generate Password", command=gerate_password)
generate_password.grid(column=2, row=3)

add = Button(text="Add", width=30, command=save)
add.grid(column=1, row=4, columnspan=2)
window.mainloop()
