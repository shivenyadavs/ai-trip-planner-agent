import requests
import os
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        description = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        return f"""
        Current Weather in {city}:
        Description: {description}
        Temperature: {temp}°C
        Humidity: {humidity}%
        """
    else:
        return "Weather data not available."
