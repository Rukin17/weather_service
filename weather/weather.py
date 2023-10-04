import requests
from weather.config import config


def get_coordinates_by_city(city_name: str) -> dict:
    get_coordinates_url = config.get_coordinates_url
    params = {
        'q': f'{city_name}, ru',
        'appid': config.appid,
        'limit': 1

    }
    result = requests.get(get_coordinates_url, params=params)

    data_by_city = result.json()

    coordinates_by_city = {}
    if 'lat' in data_by_city[0] and 'lon' in data_by_city[0]:
        coordinates_by_city['lat'] = data_by_city[0]['lat']
        coordinates_by_city['lon'] = data_by_city[0]['lon']
        return coordinates_by_city
    else:
        raise ValueError('Координаты отсутствуют')
    

def get_weather_by_coordinates(coordinates: dict):
    weather_url = config.weather_url
    params = {
        'lat': coordinates['lat'],
        'lon': coordinates['lon'],
        'appid': config.appid,
        'units': 'metric',
        'lang': 'ru'
        
    }

    result = requests.get(weather_url, params=params)
    return result.json()
