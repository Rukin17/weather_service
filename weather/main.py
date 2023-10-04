from fastapi import FastAPI
from weather.weather import get_coordinates_by_city, get_weather_by_coordinates

app = FastAPI()

@app.get('/weather/')
def read_root():
    coordinates = get_coordinates_by_city('Moscow')
    weather = get_weather_by_coordinates(coordinates=coordinates)
    result = {
        'city': 'Moscow', 
        'temp': round(weather['main']['temp'], 1)
        }
    
    return result
