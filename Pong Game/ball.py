from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(6)
        self.setheading(random.choice([random.randrange(130, 220), random.randrange(0, 220)]))

    def move(self):
        self.forward(10)
        # self.goto(self.xcor()+10, self.ycor()+10)
        # if self.distance(x=None, y=300) < 10:
        #     self.goto(self.xcor() + 10, self.ycor() - 10)
        # if self.distance()

    def paddle_bounce_calc(self):
        if self.heading() <= 180:
            return 180 - self.heading()
        else:
           return 360 - (self.heading() - 180)