# uncomment code while uploading on python anyware proxy reason
import requests
import os
from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = ""


weather_params = {
    "lat": 30.854471,
    "lon": 75.891488,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 600:
        will_rain = True

# proxy_client = TwilioHttpClient()
# proxy_client.session.proxies = {'https':os.environ['https_proxy']}
if will_rain:
    account_sid = ""
    auth_token = ""
    client = Client(account_sid, auth_token)
    # client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
                    .create(
                        body="Take Umberalla before you go out",
                        from_='',
                        to=''
                    )
    print(message.sid)
