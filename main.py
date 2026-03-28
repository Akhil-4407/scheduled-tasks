import os
import requests
from twilio.rest import Client
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
api_key = os.environ.get("OWM_API_KEY")
PARAMETERS= {
    "lat": 17.366,
    "lon":  78.476,
    "appid":api_key,
    "cnt":4
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=PARAMETERS)
response.raise_for_status()
data = response.json()
codes = []
for i in data["list"]:
    codes.append(i["weather"][0]["id"])
will_rain = False
for code in codes:
    if code < 600:
        will_rain = True
        break
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body="Rain expected today. Bring an Umbrella.",
    from_="whatsapp:+14155238886",
    to="whatsapp:+918977990204",
    )
    print(message.status)
