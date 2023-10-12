from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from weather.weather import OpenWeatherClient
from weather.config import config
from weather.weather import OpenWeatherError




app = FastAPI()


@app.exception_handler(OpenWeatherError)
def openweather_exception_handler(request: Request, exc: OpenWeatherError):
    return JSONResponse(
        status_code = exc.status,
        content = {'message': f'Oops! {exc.reason}'}
    )

@app.get('/weather/{city_name}/')
def get_weather_by_city(city_name: str):
    open_weather = OpenWeatherClient(url=config.open_weather_url, appid=config.appid)
    coordinates = open_weather.get_coordinates_by_city(city_name=city_name)    
    weather = open_weather.get_weather_by_coordinates(city_name=city_name, coordinates=coordinates)

    return weather

