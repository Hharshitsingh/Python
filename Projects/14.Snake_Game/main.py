from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collison with food
    if snake.head.distance(food) < 20:
        print("collide")
        food.regenrate_food()
        snake.extend()
        score.increase_score()

    # detect wall collison
    if snake.head.xcor() > 400 or snake.head.xcor() < -400 or snake.head.ycor() > 400 or snake.head.ycor() < -400:
        score.reset()
        snake.reset()

    # detect collison with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()


screen.exitonclick()
