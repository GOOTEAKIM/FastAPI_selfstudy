from model import Creature
from fastapi import FastAPI

# uvicorn web:app --reload

app = FastAPI()

@app.get("/creature")
def get_all() -> list[Creature]:
    from data import get_creatures
    return get_creatures()