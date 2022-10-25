from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

LEFT_START = (-350,0)
RIGHT_START = (350,0)

screen = Screen()
screen.tracer(0)
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
ball = Ball()
ball.rand_start()
r_paddle = Paddle(RIGHT_START)
l_paddle = Paddle(LEFT_START)
player_1 = Scoreboard((-330, -280), "Player 1")
player_2 = Scoreboard((330, -280), "Player 2")
screen.listen()
screen.onkey(r_paddle.go_up, "i")
screen.onkey(r_paddle.go_down, "k")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.update()

game_is_on = True

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce()
    if ball.xcor() <= -400 or ball.xcor() >= 400:
        if ball.xcor() <= -400:
            player_2.increase_score()
        else:
            player_1.increase_score()
        time.sleep(2)
        ball.home()
        l_paddle.goto(LEFT_START)
        r_paddle.goto(RIGHT_START)
        ball.ball_speed = 0.1
    if ball.xcor() >= 330 and ball.distance(r_paddle) <= 60 or ball.xcor() <= -330 and ball.distance(l_paddle) <= 60:
        ball.hit_paddle()





screen.exitonclick()
