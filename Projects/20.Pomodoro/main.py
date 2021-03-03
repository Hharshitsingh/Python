import tkinter as tk
import time
import math
from typing import Text
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 30
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    # global timer
    global reps
    window.after_cancel(timer)
    canvs.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_mark.config(text="")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 4 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_minute = math.floor(count/60)
    count_seconds = count % 60
    show_window = f"{count_minute}:{count_seconds}"
    if show_window == "0:8":
        window.call('wm', 'attributes', '.', '-topmost', True)
        window.after_idle(window.call, 'wm', 'attributes', '.', '-topmost', False)

    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    canvs.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")

    if count > 0:
        global timer
        timer = window.after(1, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/4)
        for _ in range(work_session):
            marks += "✔"
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodora")
# window.geometry("500x500")
window.config(padx=100, pady=50, bg=YELLOW)
# window.lift()
# photo = tk.PhotoImage(file = "./ICON.ico")
# window.iconphot(o(False, "./ICON.ico")
window.iconbitmap("./ICON.ico")
title_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW,
                       font=(FONT_NAME, "40", "bold"))
title_label.grid(column=1, row=0)


canvs = tk.Canvas(width=202, height=225, bg=YELLOW, highlightthickness=0)
pic = tk.PhotoImage(file="./tomato.png")
canvs.create_image(100, 112, image=pic)
timer_text = canvs.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvs.grid(column=1, row=1)

cmplt_work_session = tk.Label(
    text="Complete Work Session", fg="Green", bg=YELLOW)
cmplt_work_session.grid(column=1, row=3)

check_mark = tk.Label(fg="Green", bg=YELLOW)
check_mark.grid(column=1, row=4)

start_button = tk.Button(
    text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tk.Button(
    text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)


window.mainloop()
