from turtle import Turtle
import random


FONT = "Ariel"
SIZE = 8

class StateName(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()

    def create_name(self, string, position):
        self.penup()
        # self.hideturtle()
        # self.goto(random.randint(-200, 200), random.randint(-150, 150))
        self.color("black")
        self.write(arg=f"{string.title()}", align="center", font=(FONT, SIZE, "normal"))
        self.goto(position)

    # def invalid_name(self):
    #     self.color()
