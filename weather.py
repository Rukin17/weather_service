import requests

def get_coordinates_by_city(city_name: str) -> dict:
    get_coordinates_url = 'http://api.openweathermap.org/geo/1.0/direct'
    params = {
        'q': f'{city_name}, ru',
        'appid': '3c2984a5815f791e351cc2b3b0c7b978',
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
    

def weather_by_city(coordinates: dict):
    weather_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'lat': coordinates['lat'],
        'lon': coordinates['lon'],
        'appid': '3c2984a5815f791e351cc2b3b0c7b978',
        'units': 'metric',
        'lang': 'ru'
        
    }

    result = requests.get(weather_url, params=params)
    return result.json()
