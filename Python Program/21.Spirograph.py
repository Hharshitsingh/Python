import turtle
import random
timmy = turtle.Turtle()
screen = turtle.Screen()
screen.title("Spirograph")
turtle.colormode(255)
timmy.speed(20)
timmy.shape("turtle")
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        # timmy.left(size_of_gap)
        timmy.setheading(timmy.heading()+size_of_gap)

draw_spirograph(5)
screen.exitonclick()