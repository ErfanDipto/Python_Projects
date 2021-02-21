from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

game_on = True
# player_1_score = 0
# player_2_score = 0
score = ScoreBoard()
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
player_1 = Paddle(-350, 0)
player_2 = Paddle(350, 0)
ball = Ball()

screen.listen()
screen.onkey(fun=player_1.go_up, key="w")
screen.onkey(fun=player_1.go_down, key="s")
screen.onkey(fun=player_2.go_up, key="Up")
screen.onkey(fun=player_2.go_down, key="Down")
sleep_time = .1

while game_on:
    time.sleep(sleep_time)
    screen.update()
    score.update_score()
    ball.move()
    # print(f" player 1 {player_1.pos()}")
    # print(f"ball {ball.pos()}")
    # print(f"Distance {ball.distance(player_1)}")
    # collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.setheading(360-ball.heading())
    # collision with paddle
    elif ball.distance(player_1) < 50 and ball.xcor() < -325:
        ball.setheading(ball.paddle_bounce_calc())
        sleep_time *= .9
        # print("Collision")
    elif ball.distance(player_2) < 50 and ball.xcor() > 325:
        ball.setheading(ball.paddle_bounce_calc())
        sleep_time *= .9
    elif ball.xcor() > 420:
        ball.home()
        score.player_1_point()
        sleep_time = .1

    elif ball.xcor() < -420:
        ball.home()
        score.player_2_point()
        sleep_time = .1

    if score.player1_score >= 10 or score.player2_score >= 10:
        score.game_over()
        game_on = False


screen.exitonclick()
