from turtle import Turtle, Screen, pendown
timmy = Turtle()
screen = Screen()
screen.title("Etch A Sketch")


def move_forward():
    timmy.forward(10)


def move_backward():
    timmy.backward(10)


def turn_left():
    new_heading = timmy.heading()+10
    timmy.setheading(new_heading)


def turn_right():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)


def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy, pendown()


screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear, "c")
screen.exitonclick()
