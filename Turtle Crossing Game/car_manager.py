from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        # super().__init__()
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle()
            car.shape("square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.setheading(180)
            car.goto(340, random.randrange(-240, 240))
            car.color(random.choice(COLORS))
            self.car_list.append(car)

    def car_move(self):
        for cars in self.car_list:
            cars.forward(self.car_speed)

    def level_increment(self):
        self.car_speed += MOVE_INCREMENT
