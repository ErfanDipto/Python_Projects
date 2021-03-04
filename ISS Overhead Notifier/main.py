import requests
import datetime as dt
import smtplib


MY_LAT = 23.724030
MY_LNG = 90.434849

my_email = "ehdipto@zohomail.com"
my_pass = "qwerty00."


def is_iss_above():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.json()
    response.raise_for_status()

    iss_latitude = float(data['iss_position']['latitude'])
    iss_longitude = float(data['iss_position']['longitude'])
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LNG-5 <= iss_longitude <= MY_LNG+5:
        return True
    else:
        return False
    # iss_position = (iss_latitude, iss_longitude)
# print(iss_position)

# response for sunrise and sunset

def is_night():
    parameter = {"lat": MY_LAT,
                 "lng": MY_LNG,
                 "formatted": 0}
    response_sun = requests.get("https://api.sunrise-sunset.org/json", params=parameter)

    sunrise_time = response_sun.json()['results']['sunrise']
    sunset_time = response_sun.json()['results']['sunset']

    sunrise_time_hr = int(sunrise_time.split("T")[1].split(":")[0])
    sunset_time_hr = int(sunset_time.split("T")[1].split(":")[0])

    now_hr = dt.datetime.now().hour
    list_hr = [sunrise_time_hr, sunset_time_hr, now_hr]
    # list_hr = [hr+24 for hr in list_hr if hr == 0]
    print(sunrise_time_hr, sunset_time_hr, now_hr)

    # if list_hr[0] > list_hr[2] > list_hr[1]:
    if sunrise_time_hr > now_hr > sunset_time:
        return True


if is_night() and is_iss_above():
    with smtplib.SMTP("smtp.zoho.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pass)
        connection.sendmail(from_addr=my_email,
                            to_addrs="ehdipto@yahoo.com",
                            msg="Subject: Go see your ISS\n\nHey! Dipto. International Space Station is above your "
                                "head now and it is night time. Go check it out.")

# print(sunrise_time_hr, sunset_time_hr, now_hr)
