from turtle import Turtle
from turtle import Turtle
import random as ra


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.regenrate_food()

    def regenrate_food(self):
        random_X = ra.randint(-380, 380)
        random_Y = ra.randint(-380, 380)
        self.goto(random_X, random_Y)
