from turtle import Turtle, Screen, color
import random
import turtle
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = True
screen = Screen()
screen.title("Turtle Racing")
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt= f"Which turtle will win thr race? Enter a color {colors}: ")
print(user_bet)
all_turtle = []
for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=-100 + (turtle_index*40))
    all_turtle.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        # if turtle.pencolor() == user_bet: #cheeting
        #     turtle.forward(1)
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                screen.textinput(title="Make your bet", prompt= f"Which turtle will win thr race? Enter a color {colors}: ")
                print("You Won!")
            else:
                print(f"You loose! Winner of race {winner} turtle")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
