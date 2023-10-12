from fastapi.testclient import TestClient
from weather.server import app
import httpx
import respx
from httpx import Response
from fastapi.responses import JSONResponse

client = TestClient(app)


def test__get_weather__raising_an_error_when_the_server_responds_differently():
    with respx.mock: 
        city_name = 'london'
        respx.get('https://api.openweathermap.org/geo/1.0/direct') % dict(json=[{}])
        
        response = client.get(f'/weather/{city_name}/')

        assert response.status_code == 500
        assert response.json() == {'message': 'Oops! openweather client validation error'}


def test__get_weather__request_success():   
    with respx.mock: 
        city_name = 'london'
        respx.get('https://api.openweathermap.org/geo/1.0/direct') % dict(json=[{'name': 'Квартал «Лондон»', 'lat': 59.9000662, 'lon': 30.51657558486518, 'country': 'RU', 'state': 'Leningrad oblast'}])
        respx.get('https://api.openweathermap.org/data/2.5/weather') % dict(json={
            'coord': {'lon': 30.5166, 'lat': 59.9001}, 
            'weather': [{'id': 803, 'main': 'Clouds', 'description': 'облачно с прояснениями', 'icon': '04n'}], 
            'base': 'stations', 
            'main': {'temp': 10.15, 'feels_like': 9.65, 'temp_min': 8.27, 'temp_max': 11.08, 'pressure': 990, 'humidity': 93}, 
            'visibility': 10000, 
            'wind': {'speed': 9, 'deg': 210}, 
            'clouds': {'all': 75}, 
            'dt': 1697044863, 
            'sys': {'type': 2, 'id': 197864, 'country': 'RU', 'sunrise': 1696998349, 'sunset': 1697036608}, 
            'timezone': 10800, 
            'id': 539839, 
            'name': 'Кудрово', 
            'cod': 200
            })
        response = client.get(f'/weather/{city_name}/')

        assert response.status_code == 200
        assert response.json() == {"city":"london","temperature":10.2}
