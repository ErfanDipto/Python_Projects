from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
import os


response = requests.get("https://www.billboard.com/charts/hot-100/2000-08-12")
# print(response)
# print(response.text)
movie_response = response.text

soup = BeautifulSoup(movie_response, features="html.parser")

# print(soup)
# print(soup["h3"]["jsx-2692754980"])
song_soup = soup.select(selector=".chart-element__information__song")
song_list = [song.getText() for song in song_soup]
print(song_list)

header_params = {"Accept-Language": "en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7,en-GB;q=0.6",
                 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                               "Chrome/89.0.4389.72 Safari/537.36"}

response = requests.get(url="https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463",
                        headers=header_params)
# print(response)
amazon_html_response = response.text
amazon_html = BeautifulSoup(amazon_html_response, features="lxml")
product_price = float(amazon_html.select_one(selector="#price_inside_buybox").getText().split('\n')[1].replace('$', ''))

my_email = "ehdipto@yahoo.com"
my_pass = "forgot"
# print(my_pass)

if product_price < 100:
    with smtplib.SMTP("outlook.office365.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pass)
        connection.sendmail(from_addr=my_email, to_addrs="ehdipto@yahoo.com",
                            msg="Subject: Amazon\n\n yo... buy. hurry")
print(product_price)
