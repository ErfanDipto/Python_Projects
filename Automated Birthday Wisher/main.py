##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas as pd
import datetime as dt
import random
import smtplib


def send_mail(name):
    letter1_path = "./letter_templates/letter_1.txt"
    letter2_path = "./letter_templates/letter_2.txt"
    letter3_path = "./letter_templates/letter_3.txt"
    letter_list = [letter1_path, letter2_path, letter3_path]
    chosen_letter = random.choice(letter_list)
    with open(chosen_letter, "r") as letter:
        letter_read = letter.read()
        letter_replaced = letter_read.replace("[NAME]", name)
    my_email = "ehdipto@zohomail.com"
    my_pass = "wFZt68AW5yR1"
    try:
        with smtplib.SMTP("smtp.zoho.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_pass)
            connection.sendmail(from_addr=my_email, to_addrs="ehdipto@yahoo.com",
                                msg=f"Subject: Wishing for birthday.\n\n{letter_replaced}")
    except TimeoutError:
        print(f"Mail sending failed to {name}")


now = dt.datetime.now()
day = now.day
month = now.month

bday_data = pd.read_csv("./birthdays.csv")
bday_data_no_na = bday_data.dropna()
for row in bday_data.iterrows():
    if row[1]['day'] == day and row[1]['month'] == month:
        print(row[1]['day'])
        print(row[1]['month'])
        send_mail(row[1]['name'])
# print(bday_data_no_na['day'])
# print(bday_data)

print(day)
print(month)


