import math
import os
from datetime import datetime
import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("API_KEY")

def get_weather(city, api_key):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city.lower()}&appid={api_key}&lang=ru&units=metric'
    responce = requests.get(url)
    
    data = responce.json()

    temp = data['main']['temp']
    feels = data['main']['feels_like']
    wind = data['wind']['speed']
    city = data['name']
    sunrise = datetime.fromtimestamp(data["sys"]["sunrise"])
    sunset = datetime.fromtimestamp(data["sys"]["sunset"])
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']

    map_to_icon = {
     "Clear": "Ясно \U00002600",
     "Clouds": "Облачно \U00002601",
     "Rain": "Дождь \U00002614",
     "Drizzle": "Дождь \U00002614",
     "Thunderstorm": "Гроза \U000026A1",
     "Snow": "Снег \U0001F328",
     "Mist": "Туман \U0001F32B"
    }

    if data['weather'][0]['main'] in map_to_icon: 
        ws = map_to_icon[data['weather'][0]['main']]
    else:
        ws = ''

    text = (
    f"{city} сейчас:\n"
    f"Температура {round(temp)} {ws}\n"
    f"Ощущается как {round(feels)}\n"
    f"Ветер {round(wind)} м\c\n"
    f"Давление {math.ceil(pressure/1.333)}\n"
    f"Влажность {humidity}\n"
    f"Восход {sunrise.strftime('%H:%M')}\n"
    f"Закат {sunset.strftime('%H:%M')}"
    )

    return text


print(get_weather("брянск", API_KEY))