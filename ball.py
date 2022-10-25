from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(2, 2)
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def rand_start(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce(self):
        self.y_move *= -1

    def hit_paddle(self):
        self.x_move *= -1
        self.ball_speed *= 0.9