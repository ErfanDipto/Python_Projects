from turtle import Screen,Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()
food = Food()
score = ScoreBoard()
game_is_on = True

# time.sleep(1)
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.snake_new_pos()
    snake.set_direction()
    snake.snake_forward()
# collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.snake_append()
        score.score_update()
# collision with wall
    elif snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        score.game_over()
        time.sleep(2)
        snake.snake_reset()
        # game_is_on = False
# detect collision with tail
    elif snake.collision_with_tail():
        score.game_over()
        time.sleep(2)
        snake.snake_reset()
        # game_is_on = False
# print(snake_body[1].pos())
    else:
        pass

screen.exitonclick()
