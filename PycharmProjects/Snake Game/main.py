from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

sc = Screen()
sc.setup(width=600, height=600)
sc.bgcolor("black")
sc.title("My Snake Game")
game_is_on = True
snake = Snake()
food = Food()
scoreboard = Scoreboard()
sc.listen()
sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
sc.onkey(snake.left, "Left")
sc.onkey(snake.right, "Right")
while game_is_on:
    sc.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.move()
        snake.extend()
        scoreboard.increase()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
    for segment in snake.segments:
        if snake.head == segment:
            pass
        elif snake.head.distance(segment) < 5:
            scoreboard.reset()
            snake.reset()

sc.exitonclick()
