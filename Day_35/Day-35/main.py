import requests
import os
from twilio.rest import Client
MY_LAT = 15.789711
MY_LAT1 = 14.582260
MY_LONG = 108.366913
MY_LONG1 = 120.974800
api_key = os.environ["OWN_API_KEY"]
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]

parameters = {
    "lat": MY_LAT1,
    "lon": MY_LONG1,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
"""
for i in range(12):
    weather_id = weather_data["hourly"][i]["weather"][0]["id"]
    if weather_id < 700:
        print("Bring an Umbrella")
        break
"""

will_rain = False
weather_slice = weather_data["hourly"][:12]
# Create a list contain weather condition within 12 hours
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from_="+19856022864",
        to="+84379536722"
    )

    print(message.status)

