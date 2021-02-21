from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        # self.paddle_list = [self.create_paddle(350, 0), self.create_paddle(-350, 0)]
        # # self.paddle_list[0].goto(350, 0)
        # # self.paddle_list[1].goto(-350, 0)
        # self.player1_paddle = self.paddle_list[1]
        # self.player2_paddle = self.paddle_list[0]
        # self.paddle = Turtle()
        self.penup()
        self.speed("fastest")
        self.shape("square")
        self.goto(x, y)
        self.shapesize(stretch_wid=5, stretch_len=1)
        # self.paddle.setheading(90)
        self.color("white")

    # def create_paddle(self, x, y):
    #     self.paddle = Turtle()
    #     self.paddle.penup()
    #     self.speed("fastest")
    #     self.paddle.shape("square")
    #     self.paddle.goto(x, y)
    #     self.paddle.shapesize(stretch_wid=5, stretch_len=1)
    #     # self.paddle.setheading(90)
    #     self.paddle.color("white")
    #     return self.paddle

    def go_up(self):
        self.goto(self.xcor(), self.ycor()+20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor()-20)

    # def go_up_p2(self):
    #     self.player2_paddle.goto(self.player2_paddle.xcor(), self.player2_paddle.ycor()+20)
    #
    # def go_down_p2(self):
    #     self.player2_paddle.goto(self.player2_paddle.xcor(), self.player2_paddle.ycor()-20)

    # def move_player2_if_comp(self):
    #     if self.player2_paddle.distance(x=350, y=280) < 10:
    #         self.player2_paddle.back(10)
    #     elif self.player2_paddle.distance(x=350, y=-280) < 10:
    #         self.player2_paddle.forward(10)
