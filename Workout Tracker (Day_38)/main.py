import requests
import datetime as dt


APP_ID = "c584d9f1"
API_KEY = "75abfdd438e01489f677c710d709349e"

user_input = input("Tell me what exercise you did: ")

natural_workout_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
header = {"x-app-id": APP_ID,
          "x-app-key": API_KEY,
          "Content-Type": "application/json"}
natural_workout_body = {"query": user_input,
                        "gender": "male",
                        "weight_kg": 54,
                        "height_cm": 167.64,
                        "age": 26}

response = requests.post(url=natural_workout_endpoint, json=natural_workout_body, headers=header)

time_now = str(dt.datetime.now()).split(" ")[1].split(".")[0]
date_today = dt.date.today().strftime("%d/%m/%Y")

try:
    duration_min = response.json()['exercises'][0]['duration_min']
    calories = response.json()['exercises'][0]['nf_calories']
    exercise_name = response.json()['exercises'][0]['name']
except IndexError:
    print("Sorry, you are not talking about any exercise")


sheety_api_endpoint = "https://api.sheety.co/50c5803c2d123cdcc877711d692cc147/myWorkouts/workouts"

sheety_header = {"Content-Type": "application/json"}

sheety_body = {"workout": {"date": date_today,
                           "time": time_now,
                           "exercise": exercise_name,
                           "duration": duration_min,
                           "calories": calories}}

response_sheety = requests.post(url=sheety_api_endpoint, json=sheety_body, headers=header)

print(response_sheety)
print(response_sheety.json())
print(response.text)
