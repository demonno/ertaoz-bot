import requests
import datetime

from bots import env


class Weather:
    weather_api_id = None

    def __init__(self):
        self.weather_api_id = env.str("WEATHER_API_ID")

    def weather_forecast(self, city):
        resp = requests.get(
            "http://api.openweathermap.org/data/2.5/weather",
            params={"q": city, "appid": self.weather_api_id, "units": "metric"},
        )

        if resp.status_code == 200:
            weather_data = resp.json()
            temp = round(weather_data["main"]["temp"])
            feels_like = round(weather_data["main"]["feels_like"])
            weather_info = weather_data["weather"][0]["description"]
            wind = weather_data["wind"]["speed"]
            timezone = weather_data["timezone"]
            sunrise = datetime.datetime.utcfromtimestamp((weather_data["sys"]["sunrise"]) + timezone)
            sunset = datetime.datetime.utcfromtimestamp((weather_data["sys"]["sunset"]) + timezone)
            sunrise_hour = sunrise.hour
            sunrise_minute = sunrise.minute
            sunset_hour = sunset.hour
            sunset_minute = sunset.minute

            result = (
                f"{city} ტემპერატურა: {temp} C \nრეალური შეგრძნება: {feels_like} C \nამინდი: {weather_info}\n"
                f"ქარის სიჩქარე: {wind} კმ/ს\nმზის ამოსვლა: {sunrise_hour}:{sunrise_minute}\n"
                f"მზის ჩასვლა: {sunset_hour}:{sunset_minute}"
            )

            return result
        else:
            return "ამინდის პროგნოზი ვერ მოიძებნა"
