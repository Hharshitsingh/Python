from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.backward(MOVE_DISTANCE)

    def left(self):
        self.setheading(180)
        self.up()
        self.setheading(90)

    def right(self):
        self.setheading(0)
        self.up()
        self.setheading(90)

    def reset_position(self):
        self.goto(STARTING_POSITION)
