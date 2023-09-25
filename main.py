from fastapi import FastAPI
from weather import get_coordinates_by_city, weather_by_city

app = FastAPI()

@app.get('/weather/')
def read_root():
    coordinates = get_coordinates_by_city('Moscow')
    weather = weather_by_city(coordinates=coordinates)
    result = {
        'city': 'Moscow', 
        'temp': round(weather['main']['temp'], 1)
        }
    # return f"Температура в Москве: {round(weather['main']['temp'], 1)} градусов Цельсия"
    return result
