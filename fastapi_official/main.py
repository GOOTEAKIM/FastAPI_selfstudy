import uvicorn
import os
from fastapi import FastAPI

from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

def create_app() -> FastAPI:
    app = FastAPI()
    return app

app = create_app()

@app.get('/')
def read_rood():
    test_env = os.environ['TEST_ENV']
    return {'result': test_env}

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0')