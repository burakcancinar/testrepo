from turtle import Screen, Turtle
from snake import Snake
from food import Food, Food2
from scoreboard import Scoreboard

import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
food2 = Food2()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

a = 0.1
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(a)
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 20:
        print("Food is eaten")
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        a -= 0.001
    #Detect collision with food2.
    if snake.head.distance(food2) < 20:
        print("Food2 is eaten")
        food2.refresh()
        snake.extend2()
        scoreboard.increase_score2()
        a -= 0.01


    #Detect collision with border.
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        scoreboard.reset()
        snake.reset()
        a = 0.1
    #Detect collision with itself.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            a = 0.1
            snake.reset()



















screen.exitonclick()
