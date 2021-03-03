from turtle import Turtle
ALINGNMENT = "center"
FONT = ("Arial", 18, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("data.txt", "r") as data:
                self.highsore = int(data.read())
        except:
            self.highsore = 0
        self.old_highscore = self.highsore
        self.color("white")
        self.penup()
        self.goto(-200, 365)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} Highscore {self.highsore}", align=ALINGNMENT, font=FONT)

    def increase_score(self):
        self.score += 10
        if self.score > self.highsore:
            self.highsore = self.score
        self.update_scoreboard()

    def reset(self):
        if self.old_highscore < self.highsore:
            print("reset")
            with open("data.txt", "w") as data:
                data.write(f"{str(self.highsore)}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALINGNMENT, font=FONT)
