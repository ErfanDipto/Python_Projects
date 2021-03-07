import requests
import datetime as dt

NEWS_API = "c150574f442841fc83a330e01ddf0637"
request_url_news = "https://newsapi.org/v2/everything"
parameter_news = {"q": "tesla",
                  "apikey": NEWS_API}

response_news = requests.get(request_url_news, params=parameter_news)
print(response_news)
print(response_news.json()['articles'][0]['title'])













STOCK_PRICE_API_KEY = "557ODKVEVLKU6MXQ"
request_url_stock_price = "https://www.alphavantage.co/query"
parameter_stock_price = {"function": "TIME_SERIES_DAILY_ADJUSTED",
             "symbol": "TSLA",
             "apikey": STOCK_PRICE_API_KEY}
response_stock_price = requests.get(request_url_stock_price, params=parameter_stock_price)

today_date = str(dt.datetime.today()).split(" ")[0]
yesterday_date = str(dt.datetime.today() - dt.timedelta(days=1)).split(" ")[0]
day_b4_ystrdy_date = str(dt.datetime.today() - dt.timedelta(days=2)).split(" ")[0]

tdy_cls_prc = float(response_stock_price.json()['Time Series (Daily)'][yesterday_date]['5. adjusted close'])
ystrdy_cls_prc = float(response_stock_price.json()['Time Series (Daily)'][day_b4_ystrdy_date]['5. adjusted close'])

price_difference = tdy_cls_prc-ystrdy_cls_prc

ten_percent = (ystrdy_cls_prc / 100) * 10

if price_difference > 0 and price_difference > ten_percent:
    print("There is more")
elif price_difference < 0 and price_difference < -ten_percent:
    print("There is less")

# print(response_stock_price)
# print(response_stock_price.json())
# print(tdy_cls_prc)
# print(ystrdy_cls_prc)
# print(ten_percent)
# print(yesterday_date)
