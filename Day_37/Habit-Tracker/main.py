import requests
from datetime import datetime

USERNAME = "vuong"
TOKEN = "vuongvlq1998"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Create Graphs:
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Study Python Graph",
    "unit": "Hour",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# print(today.strftime("%Y%m%d"))
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many time did you study Python today? "),
}

response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
print(response.text)

# Update yesterday's data (20220627) to a new value (3 to 4) using an HTTP put request:
day_update = datetime(year=2022, month=6, day=27).strftime("%Y%m%d")
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{day_update}"

update_data = {
    "quantity": "4",
}

# response = requests.put(url=update_endpoint, json=update_data, headers=headers)
# print(response.text)

# Delete data:
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{day_update}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)

