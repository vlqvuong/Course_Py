import requests
from datetime import datetime

MY_LAT = 14.058324
MY_LONG = 108.277199
"""response = requests.get(url="http://api.open-notify.org/iss-now.json")
# Get data we want from the endpoint
# print(response)
# Response Code:
# 1XX: Hold on, something's happening, this is not final.
# 2XX: Here you go. Every thing was successful.
# 3XX: Go away. You don't actually have permission to get this thing
# 4XX: You Screwed up. EX:404. The thing you're looking for doesn't even exist.
# 5XX: I screwed up. The server that you are making the request to, screwed up.

# if response.status_code != 200:
#     raise Exception("Bad response from ISS API")

response.raise_for_status()
# Raise an HTTPError if the HTTP request returned an un-successful status code.

# Get the actual data from API:
# data = response.json()
# print(data)

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (longitude, latitude)

print(iss_position)"""

# API Parameters: Allow to give an input. Get different pieces of data back depending on input.
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.now()

print(time_now.hour)

