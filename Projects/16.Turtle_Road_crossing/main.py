import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Road Crossing")
screen.bgcolor("black")
play = Player()

car_manager = CarManager()
score = Scoreboard()
game_is_on = True

screen.listen()
screen.onkey(play.up, "Up")
screen.onkey(play.down, "Down")
screen.onkey(play.left, "Left")
screen.onkey(play.right, "Right")

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()
    
    # reach turtle to finish
    if play.ycor() > 280:
        score.increse_score()
        play.reset_position()
        car_manager.level_up()

    # detect collision with car
    for car in car_manager.all_cars:
        if car.distance(play) < 20:
            game_is_on = False
            score.game_over()


screen.exitonclick()
