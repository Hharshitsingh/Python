import turtle
from turtle import Screen, Turtle
from random import randint, random

class Shapes (Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.screen = Screen()
        self.screen.title("Turtle Shapes")
        self.screen.setup(width=680, height=700)
        self.screen.bgcolor("black")
        turtle.colormode(255)
        self.color(self.random_color())
        self.penup()
        self.goto(-50, 300)
        self.pendown()
        self.start_drawing()
        self.screen.exitonclick()

    def start_drawing(self):
        for num_of_side in range(3, 21):
            self.draw_shape(num_of_side)
        self.hideturtle()

    def draw_shape(self, numofside):
        self.speed(5.5)
        self.color(self.random_color())
        for _ in range(numofside):
            angle = 360/numofside
            self.forward(100)
            self.right(angle)

    def random_color(self):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        color = (r, g, b)
        return color

start = Shapes()
