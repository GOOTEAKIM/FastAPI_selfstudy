from fastapi import FastAPI, Depends, Path, HTTPException
from pydantic import BaseModel
from database import engineconn
from models import Test, Base

app = FastAPI()

engine = engineconn()
session = engine.create_session()

Base.metadata.create_all(bind=engine.engine)

class Item(BaseModel):
    name: str
    number: int

@app.get("/")
async def first_get():
    example = session.query(Test).all()
    return example

@app.post("/add_item/")
async def add_item(item: Item):
    new_item = Test(name=item.name, number=item.number)
    session.add(new_item)
    session.commit()
    return {"message": "Item added successfully"}