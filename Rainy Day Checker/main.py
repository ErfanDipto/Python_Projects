import requests
import os
# from  twilio.rest import Client

MY_API = os.environ['my_api']
MY_LAT = 23.723460
MY_LNG = 90.435493
exclude = "current,minutely,daily"


# def send_message():
#     twilio_phn_number = "+15015751049"
#     my_phn_number = "+8801521333595"
#     t_sid = "AC6d9dc637964d4bc70c604bbc834cef86"
#     t_auth = "eabf2e18a53376d74fe2fbee4f445092"
#     client = Client(t_sid, t_auth)
#
#     message = client.messages.create(body="please bring an today umbrella if you go out",
#                                      from_=twilio_phn_number, to=my_phn_number)


rainy_lat = 36.191
rainy_lng = 160.730

parameter = {"lat": rainy_lat,
             "lon": rainy_lng,
             "appid": MY_API,
             "exclude": exclude}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameter)
response.raise_for_status()
weather_data = response.json()
weather_id_list = []
for i in range(0, 12):
    weather_id_list.append(weather_data['hourly'][i]['weather'][0]['id'])

is_rain = False

for ids in weather_id_list:
    if ids < 700:
        is_rain = True
if is_rain:
    # send_message()
    print("Please bring an today umbrella if you go out")

# print(response)
# print(weather_data)

print(weather_id_list)
