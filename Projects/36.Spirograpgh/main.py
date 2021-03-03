import turtle
from turtle import Turtle, Screen
from random import randint


class Spirograpgh (Turtle):
    def __init__(self, gap_size):
        super().__init__()
        self.gap_size = gap_size
        self.shape("turtle")
        self.screen = Screen()
        self.screen.title("Spirograpgh")
        self.screen.bgcolor("black")
        turtle.colormode(255)
        self.draw_spirograph()
        self.screen.exitonclick()

    def draw_spirograph(self):
        self.speed(10)
        for _ in range(int(360/self.gap_size)):
            self.color(self.random_color())
            self.circle(100)
            self.setheading(self.heading()+self.gap_size)

    def random_color(self):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        color = (r, g, b)
        return color


start = Spirograpgh(gap_size=25)




