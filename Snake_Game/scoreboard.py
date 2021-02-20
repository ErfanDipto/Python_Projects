from turtle import Turtle



ALIGNMENT = "center"
FONT = "Courier"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.initial_score = 0
        with open("data.txt") as data:
            # data.write("0")
            self.high_score = int(data.read())
        # self.high_score = int(high_score_data)
        self.score = Turtle()
        self.score.hideturtle()
        self.score.color("White")
        self.score.speed("fastest")
        self.score.penup()
        self.score.goto(-10, 260)
        # self.score.write(f"Score: {self.initial_score}", align=ALIGNMENT, font=(FONT, 24, "normal"))
        self.update_scoreboard()

    def update_scoreboard(self):
        self.score.clear()
        self.score.write(f"Score: {self.initial_score} High Score: {self.high_score}", align=ALIGNMENT, font=(FONT, 24,
                                                                                                              "bold"))

    def score_update(self):
        self.initial_score += 1
        self.update_scoreboard()

    def game_over(self):
        if self.initial_score > self.high_score:
            self.high_score = self.initial_score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score.clear()
        self.score.write(f"Score: {self.initial_score} High Score: {self.high_score}", align=ALIGNMENT, font=(FONT, 24,
                                                                                                              "bold"))
        # self.game_over_speech = Turtle()
        # self.game_over_speech.hideturtle()
        # self.game_over_speech.color("White")
        # self.game_over_speech.speed("fastest")
        # self.game_over_speech.penup()
        # self.game_over_speech.goto(-10, 0)
        # self.game_over_speech.write("Game Over", align=ALIGNMENT, font=(FONT, 35, "bold"))
