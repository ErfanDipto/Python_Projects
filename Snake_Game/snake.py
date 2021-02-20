from turtle import Turtle, Screen

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):

        self.screen = Screen()

        self.snake_body = []
        for i in range(3):
            self.snake_body.append(self.snake_create())
            self.snake_body[i].setx(i * -20)
        self.head = self.snake_body[0]

    def snake_create(self):
        self.snakee = Turtle()
        # self.snakee.home()
        self.snakee.shape("square")
        self.snakee.speed(15)
        self.snakee.penup()
        self.snakee.color("white")
        return self.snakee

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def set_direction(self):
        self.screen.listen()
        self.screen.onkey(key="w", fun=self.move_up)
        self.screen.onkey(key="s", fun=self.move_down)
        self.screen.onkey(key="a", fun=self.move_left)
        self.screen.onkey(key="d", fun=self.move_right)

    def snake_forward(self):
        self.head.forward(MOVE_DISTANCE)

    def snake_append(self):
        self.snake_body.append(self.snake_create())
        self.snake_body[-1].setpos(self.snake_body[-2].pos())

    def snake_new_pos(self):
        for i in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[i].setpos(self.snake_body[i - 1].pos())

    def collision_with_tail(self):
        for body_part in self.snake_body[1:]:
            # if body_part == self.head:
            #     pass
            if self.head.distance(body_part) < 10:
                return True

    def snake_reset(self):
        for body_parts in self.snake_body:
            body_parts.goto(1000, 1000)
        self.snake_body.clear()
        for i in range(3):
            self.snake_body.append(self.snake_create())
            self.snake_body[0].setpos(0, 0)
            self.snake_body[i].setx(i * -20)
