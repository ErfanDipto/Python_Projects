import turtle
import pandas as pd
import state_name


screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
screen.title("U.S. States Game")
turtle.shape(image)
state__name = state_name.StateName()
game_is_on = True


data = pd.read_csv("50_states.csv")
states_list = data["state"].to_list()
correct_guess_list = []
# missing_state_list = []
# print(states_list)
# cal = "california"
# state_row = data[data["state"] == f"{cal.capitalize()}"]
# state_pos = (int(state_row["x"]), int(state_row["y"]))
# if data["state"].str.contains(f"{cal.title()}").any():
#     print("Yes")

# print(screen.screensize())
player_score = 0

while len(correct_guess_list) < 50:
    answer_text = screen.textinput(title=f"{player_score}/50 States Correct", prompt="Please insert state name: ")
    if data["state"].str.contains(f"{str(answer_text).title()}").any():
        if answer_text.title() in correct_guess_list:
            pass
        else:
            state_row = data[data["state"] == f"{answer_text.title()}"]
            state_pos = (int(state_row["x"]), int(state_row["y"]))
            state__name.create_name(answer_text, state_pos)
            player_score += 1
            correct_guess_list.append(answer_text.title())
    elif answer_text.lower() == "exit":
        break

# for states in states_list:
#     if states not in correct_guess_list:
missing_state_list = [states for states in states_list if states not in correct_guess_list]

missing_states = pd.DataFrame(missing_state_list)
missing_states.to_csv("Missing States.csv")

# with open("Missing States.csv", mode="w") as missing:
#     missing.write(missing_states)
screen.exitonclick()
