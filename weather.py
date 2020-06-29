import requests
import json
from dotenv import load_dotenv
import os
import time

load_dotenv()
api_key = os.getenv('api_key')
city_name = input('>>>')


def weather_report(api_key, city_name):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
    res = requests.get(url)
    data = json.loads(res.text)
    city = data['name']
    weather = data['weather'][0]['main']  # description of weather
    temperature = data['main']['temp']-273.15  # kelvin to celcius
    feels_like = round((data['main']['feels_like']-273.15), 1)  # in degrees
    wind_speed = data['wind']['speed']  # reads in m/s
    wind_direction = data['wind']['deg']  # wind direction in degrees
    pressure = data['main']['pressure']  # to be read in hpa
    humidity = data['main']['humidity']  # percentage
    # unix time for sunrise/sunset, convert to asctime
    sunrise = time.asctime(time.localtime(data['sys']['sunrise']))
    sunset = time.asctime(time.localtime(data['sys']['sunset']))
    print(f'In {city} the temperature is {temperature} degrees celcius.\nThe weather is {weather}\nIt feels like {feels_like}\nThe humidity is {humidity}%')


weather_report(api_key, city_name)
