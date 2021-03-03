import tkinter as tk
CANVAS_FONT = "Times 12 italic"
CANVAS_TITTLE_FONT = "Arial 18 bold"
WINDOW_BACKGROUND = "#03045e"
CANVAS_BACKGROUND = "#023e8a"
class Game:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("ROCK PAPER SCISSOR")
        self.window.config(padx=20, pady=20, bg=WINDOW_BACKGROUND)

        self.title_canvas = tk.Canvas(width=400, height=120, bg=CANVAS_BACKGROUND, highlightthickness=0)
        self.title_canvas.grid(row=0, column=0, columnspan=3)
        self.title_canvas.create_text(20, 30, text = "ROCK", anchor = "w", font = CANVAS_TITTLE_FONT)
        self.title_canvas.create_text(20, 60, text = "PAPER", anchor = "w", font = CANVAS_TITTLE_FONT)
        self.title_canvas.create_text(20, 90, text = "SCISSOR", anchor = "w", font = CANVAS_TITTLE_FONT)
        self.title_canvas.create_text(300, 30, text = "SCORE", anchor = "w", font = CANVAS_TITTLE_FONT)
        self.title_canvas.create_text(340, 70, text = "0", anchor = "center", font = CANVAS_TITTLE_FONT)

        



        self.window.mainloop()


start = Game()
start
