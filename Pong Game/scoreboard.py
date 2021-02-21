from turtle import Turtle
ALIGNMENT = "center"
FONT = "courier"
SIZE = 80


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        # Screen().bgcolor("black")
        self.penup()
        self.hideturtle()
        self.color("white")
        self.player1_score = 0
        self.player2_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.player1_score}", align=ALIGNMENT, font=(FONT, SIZE, "bold"))
        self.goto(100, 200)
        self.write(f"{self.player2_score}", align=ALIGNMENT, font=(FONT, SIZE, "bold"))

    def player_1_point(self):
        self.player1_score += 1
        self.update_score()

    def player_2_point(self):
        self.player2_score += 1
        self.update_score()

    def game_over(self):
        if self.player1_score > self.player2_score:
            highest_scorer = "Player 1"
        else:
            highest_scorer = "Player 2"
        self.home()
        self.write(f"  GAME OVER \n{highest_scorer} Wins!".center(0, "\n"), align=ALIGNMENT, font=(FONT, 20, "bold"))
