import uvicorn
from weather.server import app

if __name__ == '__main__':
    uvicorn.run(app)