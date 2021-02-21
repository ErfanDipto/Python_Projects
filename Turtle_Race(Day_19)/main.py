from turtle import Turtle, Screen
import random

race_is_on = False
screen = Screen()
screen.screensize(500, 500)
michy = Turtle()
raph = Turtle()
leo = Turtle()
donny = Turtle()
michy.color("Orange")
raph.color("Red")
leo.color("Blue")
donny.color("Indigo")
turtle_dict = {"Michy": michy, "Raph": raph, "Leo": leo, "Donny": donny}
user_bet = Screen().textinput(title="Place your bet", prompt="Select one of them (Michy/Raph/Leo/Donny): ")
if user_bet.lower() == "michy" or user_bet.lower() == "raph" or user_bet.lower() == "leo" or user_bet.lower() == "donny":
    race_is_on = True
else:
    print("Invalid Input")


def turtle_pos(t, x, y):
    t.shape("turtle")
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.setpos(x, y)
    t.showturtle()


# def check_bet():
#     if user_bet:
#         # print(f"{keys} won the race!")
#         return False
#     else:
#         return True


turtle_pos(michy, -300, 200)
turtle_pos(raph, -300, 50)
turtle_pos(leo, -300, -100)
turtle_pos(donny, -300, -250)
# print(michy.xcor())

while race_is_on:
    for key, value in turtle_dict.items():
        if value.xcor() >= 300:
            race_is_on = False
            if key.lower() == user_bet.lower():
                print("You have won the bet!")
            else:
                print("You have lost the bet.")
            print(f"{key} won the race.")
        value.forward(random.randrange(0, 10))
        # check_finish_line(turtle_dict)

screen.exitonclick()
