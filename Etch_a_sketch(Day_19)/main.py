from turtle import Turtle, Screen


turtle = Turtle()
screen = Screen()
screen.screensize(500, 500)
# turtle.setheading(-90)


def forward():
    turtle.forward(10)


def backward():
    turtle.back(10)


def turn_anti_clk():
    turtle.right(20)


def turn_clk():
    turtle.left(20)


def clear():
    turtle.reset()
    screen.reset()


screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=turn_anti_clk)
screen.onkey(key="d", fun=turn_clk)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
