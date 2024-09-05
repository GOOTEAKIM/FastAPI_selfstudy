from datetime import datetime
from typing import Union, List

from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

fake_db = {}

class Item(BaseModel):
    title: str
    timestamp: datetime
    description: Union[str, None] = None

app =FastAPI()

@app.put('/items/{id}')
def update_item(id: str, item:Item):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data

@app.get('/items/', response_model=List[Item])
def get_all_items():
    if fake_db:
        return list(fake_db.values())  
    else:
        raise HTTPException(status_code=404, detail="No items found")