from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("black")

    def show_level(self):
        self.goto(-250, 250)
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def level_update(self):
        self.level += 1
        # self.clear()
        self.show_level()

    def game_over(self):
        self.home()
        # self.clear()
        self.write("GAME OVER", align="center", font=FONT)
