import requests
import datetime as dt

token = "qwertyuiopasdfghjklzxcvbnm"
pixela_endpoint = "https://pixe.la/v1/users"
user_name = "erfandipto"
parameters = {"token": token,
              "username": user_name,
              "agreeTermsOfService": "yes",
              "notMinor": "yes"}
# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response)
# print(response.text)
# print(response.json())
graph_endpoint = f"{pixela_endpoint}/{user_name}/graphs"
graph_id = "graph1"

graph_config = {"id": graph_id,
                "name": "Walking Exercise",
                "unit": "km",
                "type": "float",
                "color": "momiji",
                "timezone": "Asia/Dhaka"}
header = {"X-USER-TOKEN": token}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)
# print(response)
# print(response.json())

today = str(dt.date.today()).replace("-", "")
yesterday_date = dt.date.today() - dt.timedelta(1)
yesterday = yesterday_date.strftime("%Y%m%d")

pixel_request_body = {"date": yesterday,
                      "quantity": "0.3"}

pixel_post_endpoint = f"{pixela_endpoint}/{user_name}/graphs/{graph_id}"

pixel_put_endpoint = f"{pixela_endpoint}/{user_name}/graphs/{graph_id}/{yesterday}"

put_post_body = {"quantity": "1.3"}

response = requests.post(url=pixel_post_endpoint, json=pixel_request_body, headers=header)
print(response)
print(response.text)
print(response.json())

# print(today)
