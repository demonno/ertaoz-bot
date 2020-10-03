import datetime

import requests

from bots import env


class DayWeather:
    date: str
    min_temp: int = 100
    max_temp: int = -100
    emoji: str
    description: str


class Weather:
    weather_api_id = None

    weather_emoji_dict = {
        "01": "☀",
        "02": "⛅",
        "03": "☁",
        "04": "☁",
        "09": "🌧️",
        "10": "🌧️",
        "11": "🌩️",
        "13": "❄",
        "50": "🌁",
    }

    def __init__(self):
        self.weather_api_id = env.str("WEATHER_API_ID")

    def weather(self, city):
        resp = requests.get(
            "http://api.openweathermap.org/data/2.5/weather",
            params={"q": city, "appid": self.weather_api_id, "units": "metric"},
        )

        if resp.status_code == 200:
            weather_data = resp.json()
            temp = round(weather_data["main"]["temp"])
            temp_emoji = "🌡️"
            feels_like = round(weather_data["main"]["feels_like"])
            weather_emoji = self.weather_emoji_dict[
                weather_data["weather"][0]["icon"][:-1]
            ]
            weather_info = weather_data["weather"][0]["description"]
            wind = weather_data["wind"]["speed"]
            wind_emoji = "🌪" if weather_data["wind"]["speed"] > 30 else "💨"
            timezone = weather_data["timezone"]
            sunrise = datetime.datetime.utcfromtimestamp(
                (weather_data["sys"]["sunrise"]) + timezone
            )
            sunrise_emoji = "🌅"
            sunset = datetime.datetime.utcfromtimestamp(
                (weather_data["sys"]["sunset"]) + timezone
            )
            sunset_emoji = "🌇"
            sunrise_hour = sunrise.hour
            sunrise_minute = sunrise.minute
            sunset_hour = sunset.hour
            sunset_minute = sunset.minute

            result = (
                f"{city} ტემპერატურა: {temp_emoji} {temp} ℃ \nრეალური შეგრძნება: {feels_like} C\n"
                f"ამინდი: {weather_emoji} {weather_info}\n"
                f"ქარის სიჩქარე: {wind_emoji} {wind} კმ/ს\nმზის ამოსვლა: {sunrise_emoji} {sunrise_hour}:{sunrise_minute}\n"
                f"მზის ჩასვლა: {sunset_emoji} {sunset_hour}:{sunset_minute}"
            )

            return result
        else:
            return "ამინდის პროგნოზი ვერ მოიძებნა"

    def weather_forecast(self, city):
        resp = requests.get(
            "http://api.openweathermap.org/data/2.5/forecast",
            params={"q": city, "appid": self.weather_api_id, "units": "metric"},
        )

        if resp.status_code == 200:
            weather_data = resp.json()

            timezone_shift = weather_data["city"]["timezone"]
            temp_list = weather_data["list"]
            result = ""
            weather_dict = {}
            for data in temp_list:
                date = datetime.datetime.utcfromtimestamp((data["dt"]) + timezone_shift)
                weather_dict[date.day] = DayWeather()

            for data in temp_list:
                date = datetime.datetime.utcfromtimestamp((data["dt"]) + timezone_shift)

                temp = round(data["main"]["temp"])
                if weather_dict[date.day].min_temp > temp:
                    weather_dict[date.day].min_temp = temp

                if weather_dict[date.day].max_temp < temp:
                    weather_dict[date.day].max_temp = temp

                weather_dict[date.day].emoji = self.weather_emoji_dict[
                    data["weather"][0]["icon"][:-1]
                ]
                weather_dict[date.day].description = data["weather"][0]["description"]
                weather_dict[date.day].date = str(date.day) + "-" + date.strftime("%B")

            for weather in weather_dict:
                result += f"{weather_dict[weather].date} {weather_dict[weather].max_temp}/{weather_dict[weather].min_temp}℃ {weather_dict[weather].emoji} {weather_dict[weather].description}\n"
            return result
        else:
            return "ამინდის პროგნოზი ვერ მოიძებნა"
