import requests
from twilio.rest import Client

OWM_ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'
api_key = "{key}"
account_sid = "{sid}"
auth_token = "{token}"
wether_params = {
    "lat" : 18.516726,
    "lon": 73.856255,
    "appid" : api_key,
    "cnt" : 4,
}

response = requests.get(OWM_ENDPOINT,params = wether_params)
response.raise_for_status()
weather_data = response.json()
#print(weather_data["list"][0]['weather'][0])
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain soon",
        from_='+13304439263',
        to='+919175862663'
    )

    print(message.status)
