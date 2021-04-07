from turtle import *
# # from turtle import Turtle, Screen, turtlesize
# turtle = Turtle()
# screen = Screen()
# screen.bgcolor("cyan")
# turtle.shape("turtle")
# turtle.color("red")
# # turtle.pencolor("black")
# turtle.speed(10)
# turtle.turtlesize(0.5,0.5,1.2)

# for i in range(1,51):
#     turtle.forward(70)
#     turtle.left(i*2+75)
#     turtle.forward(280)
#     turtle.circle(15)
#     turtle.goto(0,0)
# turtle.forward(150)
# turtle.left(90)
# turtle.backward(100)
# turtle.right()

# screen.exitonclick()

color('red', 'yellow')
begin_fill()
# from turtle import *
while True:
    forward(300)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()