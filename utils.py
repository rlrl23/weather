from __future__ import annotations

import requests

from config import KEY_WEATHER


def get_coordinates(city_name: str):
    url_coordinates = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={KEY_WEATHER}'
    response = requests.get(url=url_coordinates)
    content = response.json()
    lat = content[0].get('lat')
    lon = content[0].get('lon')
    return lat, lon


def get_weather(lat: float, lon: float):
    url_weather = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&lang=ru&appid={KEY_WEATHER}'
    response = requests.get(url=url_weather)
    content = response.json()
    temp = content.get('main').get('temp')
    feels_like = content.get('main').get('feels_like')

    weather = content.get('weather')[0]['description'].capitalize()
    return temp, feels_like, weather
