from typing import Annotated, Union

from fastapi import FastAPI, Path, Body
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name:str
    description: Union[str,None]=None
    price:float
    tax:Union[float,None]=None

class User(BaseModel):
    username: str
    full_name: Union[str, None] = None

'''
@app.put("/items/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: Union[str, None] = None,
    item: Union[Item, None] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results
'''

'''
json
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2
}
'''

'''
@app.put('/items/{item_id}')
async def update_item(item_id:int, item: Item, user: User):
    results = {'item_id':item_id, "item":item, 'user': user}
    return results
'''

'''
json

{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    }
}
'''

'''
@app.put('/items/{item_id}')
async def update_item(
    item_id: int, item: Item, user:User, importance: Annotated[int, Body()]
):
    results = {'item_id': item_id, 'item': item, 'user': user, 'importance': importance}
    return results
'''
    
'''json
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    },
    "importance": 5
}
'''

'''
@app.put('/items/{item_id}')
async def update_item(
    *,
    item_id:int,
    item:Item,
    user:User,
    importance: Annotated[int, Body(gt=0)],
    q: Union[str,None] = None,
):
    results = {'item_id': item_id, 'item': item, 'user': user, 'importance': importance}

    if q:
        results.update({'q':q})
    return results
    
'''

# http://127.0.0.1:8000/items/35?q=kim

'''json
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    },
    "importance": 5
}
'''

@app.put('/items/{item_id}')
async def update_item(item_id:int, item: Annotated[Item, Body(embed=True)]):
    results = {'item_id': item_id, 'item': item}
    return results

'''json
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    }
}
'''