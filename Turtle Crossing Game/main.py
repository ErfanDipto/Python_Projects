import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


car_manager = CarManager()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
score = Scoreboard()
# car1 = CarManager()
# car2 = CarManager()
# car_list = []


screen.listen()
screen.onkey(fun=player.move, key="Up")
screen.onkey(fun=player.move_back, key="Down")

# iteration = 0
game_is_on = True

while game_is_on:
    # iteration += 1
    time.sleep(0.1)
    screen.update()
    score.show_level()
    car_manager.create_car()
    car_manager.car_move()
    for cars in car_manager.car_list:
        if player.distance(cars) < 30:
            game_is_on = False
            score.game_over()
            print(f"{cars} Collided.")
    # if iteration % 6 == 0:
    #     car_list.append(CarManager())

    # for cars in car_list:
    #     cars.car_move()
    #     if player.distance(cars) < 30:
    #         print(f"Collided {cars}")
    #collision with cars


    if player.finish_line():
        time.sleep(1)
        car_manager.level_increment()
        score.level_update()
        player.go_to_start()
        print("Level finished")

screen.exitonclick()