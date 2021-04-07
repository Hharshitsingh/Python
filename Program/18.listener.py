import turtle
tim = turtle.Turtle()
timmy = turtle.Turtle()
screen = turtle.Screen()
tim.shape("turtle")
timmy.color("red")

def move_forward():
    tim.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()
