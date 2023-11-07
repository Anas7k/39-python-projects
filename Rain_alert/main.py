import requests
from twilio.rest import client # there are many ways to get an alert like telegram bot and so on.

OWM_Endpoint = "https://api.openweathermap.org/data/2.8/onecall"
account_sid = "from you 'twilio' account"
auth_token = "from your 'twilio' account"

api_key = "from your 'openweathermap' account"
weather_params = {
    "lat": 32.715736,
    "lon": -117.161087,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="it's goint to rain today. Remember to bring an ☔",
        from_="+123456789",
        to="+123456789"
    )
    print(message.status)
# then use "pythonanywhere" to run your code everyday
