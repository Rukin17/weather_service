import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Config:
    appid: str
    weather_url: str
    get_coordinates_url: str


def load():
    return Config(
        appid=os.environ['APPID'],
        weather_url=os.getenv('WEATHER_URL'),
        get_coordinates_url=os.getenv('GET_COORDINATES_URL')
    )

config = load()