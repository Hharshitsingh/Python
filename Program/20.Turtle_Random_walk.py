import turtle as t
from random import randint, choice
timmy = t.Turtle()
screen = t.Screen()
screen.title("Turtle Random Walk")
t.colormode(255)
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
direction = [0,90,180,270]
degr = ["left", "right"]
timmy.speed(10)

for _ in range(200):
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    timmy.color(r,g,b)
    pen = randint(5,10)
    timmy.pensize(pen)
    timmy.forward(20)
    timmy.setheading(choice(direction))

screen.exitonclick()