import os
import requests
import configparser

user = os.environ.get("USER")
config = configparser.ConfigParser()
config.read(f'/Users/{user}/.api/openweather/config.ini')
api_key = config['owmap']['api_key']

OMW_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

# location set to Eugene, Or
weather_params = {
    "lat": 44.052071,
    "lon": -123.086754,
    "cnt": 4,
    "appid": api_key,
}
forecasted_rain = False
response = requests.get(OMW_Endpoint, params=weather_params)
print(response.raise_for_status())
weather_data = response.json()
print(weather_data)
print(f'{weather_data["city"]["name"]}, {weather_data["city"]["country"]}')

for hour_data in weather_data["list"]:
    if hour_data["weather"][0]["id"] < 700:
        forecasted_rain = True

if forecasted_rain:
    print("Bring an Umbrella!!")
