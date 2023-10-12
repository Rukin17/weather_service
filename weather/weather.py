import httpx
from dataclasses import dataclass
from pydantic import BaseModel, ValidationError


class OpenWeatherError(Exception):
    def __init__(self, reason: str, status: int) -> None:
        super().__init__(reason, status)
        self.reason = reason
        self.status = status


class Coordinates(BaseModel):
    lat: float
    lon: float


@dataclass
class TemperatureByCity:
    city: str
    temperature: float


class OpenWeatherClient:
    def __init__(self, url, appid):
        self.url = url
        self.appid = appid

    def get_coordinates_by_city(self, city_name: str) -> Coordinates:

        params: dict[str, str | int] = {
            'q': f'{city_name}, ru',
            'appid': self.appid,
            'limit': 1

        }
        response = httpx.get(f'{self.url}/geo/1.0/direct', params=params)
        response.raise_for_status()
        data_by_city = response.json()

        try:
            coordinates_by_city = Coordinates(
                lat=data_by_city[0]['lat'], 
                lon=data_by_city[0]['lon']
                )
            return coordinates_by_city
        except KeyError as err:
            raise OpenWeatherError(reason='openweather client validation error', status=500) from err   
        except ValidationError as err:
            raise OpenWeatherError(reason='openweather client validation error', status=500) from err
       

    def get_weather_by_coordinates(self, city_name: str, coordinates: Coordinates) -> TemperatureByCity:
        params = {
            'lat': coordinates.lat,
            'lon': coordinates.lon,
            'appid': self.appid,
            'units': 'metric',
            'lang': 'ru'
        }

        result = httpx.get(f'{self.url}/data/2.5/weather', params=params).json()
        weather = TemperatureByCity(city=city_name, temperature=round(result['main']['temp'], 1))
        print(result)
        return weather
