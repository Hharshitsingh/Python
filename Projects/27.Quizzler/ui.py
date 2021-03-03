from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = 0
        self.score_ui = Label(
            text=f"Score: {self.score}", fg="white", bg=THEME_COLOR)
        self.score_ui.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, text="some Question", 
            width=280,
            fill=THEME_COLOR, 
            font=("Arial", 20, "italic")
            )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_image,highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)
        false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_image,highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text = "End of quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.score += 1
            self.canvas.config(bg="green")
            self.score_ui.config(text=f"Score {self.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(500, self.get_next_question)

