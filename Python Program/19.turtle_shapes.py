import turtle
import random
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.title("Turtle Shapes")
timmy = turtle.Turtle()
timmy.shape("turtle")
timmy.color("red")
# square
# for _ in range(4):
#     timmy.forward(200)
#     timmy.right(90)

# Dashed line
# for _ in range(10):
#     timmy.pencolor("black")
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()



turtle.speed(15)
turtle.colormode(255)
timmy.penup()
timmy.goto(-100,300)
timmy.pendown()
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color
def draw_shape(numofside):
    num_sides = numofside
    for _ in range(num_sides):
        angle = 360/num_sides
        timmy.forward(100)
        timmy.right(angle)


for i in range(3, 20):
    timmy.color(random_color())
    draw_shape(i)


screen.exitonclick()
