from typing import Set, Union

from fastapi import FastAPI, status
from pydantic import BaseModel

from enum import Enum

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price : float
    tax : Union[float, None ]=None
    tags : set[str] = set()

class Tags(Enum):
    items = 'items'
    users = 'users'

# @app.post('/items/', response_model=Item, tags=['items'])
# async def create_item(item: Item):
#     return item

# @app.get('/items/', tags=["items"])
# async def read_items():
#     return [{'name': 'Foo', 'price': 42}]

# @app.get('/users/', tags=['users'])
# async def read_users():
#     return [{'username': 'johndoe'}]

@app.get('/items/', tags=[Tags.items])
async def get_items():
    return ['Portal gun', 'Plumbus']

@app.get('/users/', tags=[Tags.users])
async def read_users():
    return ['Rick', 'Morty']

@app.post("/items/", response_model=Item, summary="Create an item")
async def create_item(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item

# 경로 작업 사용 중단

@app.get('/elements/', tags=['items'], deprecated=True)
async def read_elements():
    return [{'item_id': 'Foo'}]