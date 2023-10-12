import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Config:
    appid: str
    open_weather_url: str


def load():
    return Config(
        appid=os.environ['APPID'],
        open_weather_url=os.environ['OPEN_WEATHER_URL'],
    )

config = load()