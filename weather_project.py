import os
import requests
from datetime import datetime

user_key = os.environ["weather_data"]
location = input("Enter the city name: ").upper()
api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + user_key
weather_data = requests.get(api_link)
api_data = weather_data.json()
if api_data["cod"] == "404":
    print("Error!! You have entered wrong city. ")

else:
    temp_city = ((api_data["main"]["temp"]) - 273.15)
    hmdt = api_data['main']['humidity']
    wind_speed = (api_data["wind"]["speed"])
    weather_dis = (api_data["weather"][0]["description"])
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    print("-------------------------------------------------------------")
    print("-------------------------------------------------------------")

    print("Weather Stats for - {}  || {} 🌅 🌦️ 🌥️ ⛈️".format(location.upper(), date_time))

    print("-------------------------------------------------------------")
    print("-------------------------------------------------------------")
    print("  ")
    print("The current temperature of  {} is  {:.2f} Degree C ".format(location, temp_city))
    print("Current Humidity :", hmdt, '%')
    print(weather_dis.upper())
    print("The wind blowing at {} km/h".format(wind_speed))
