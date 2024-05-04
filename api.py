import os
import requests
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("API_KEY")

def get_weather(city, api_key):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=ru&units=metric'
    responce = requests.get(url)
    
    data = responce.json()

    heaven = data['weather'][0]['description']
    temp = data['main']['temp']
    feels = data['main']['feels_like']
    wind = data['wind']['speed']

    text = (
    f"{city.capitalize()} сейчас:\n"
    f"Температура: {round(temp)}\n"
    f"Ощущается как {round(feels)}\n"
    f"Ветер: {round(wind)} м\c\n"
    f"На небе: {heaven}"
    )

    return text





print(get_weather("брянск", api_key))