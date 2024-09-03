from enum import Enum
from fastapi import FastAPI

app = FastAPI()

class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'

# 경로 매개변수

@app.get('/')
async def root():
    return {'message': 'Hello World'}

# @app.get("/items/{item_id}")
# async def read_item(item_id : int):
#     return {"item_id":item_id}

@app.get('/users')
async def read_users():
    return ['Rick', 'Morty']

@app.get('/users/me')
async def read_user_me():
    return{'user_id': 'the current user'}

@app.get('/users/{user_id}')
async def read_user(user_id: str):
    return {"user_id": user_id}

@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {'model_name': model_name, 'message': 'Deep Learning FTW!'}

    if model_name.value == 'lenet':
        return {'model_name': model_name, 'message': 'LeCNN all the images'}
    
    return {'model_name': model_name, 'message' : 'Have some residuals'}

@app.get('/files/{file_path:path}')
async def read_file(file_path: str):
    return {'file_path': file_path}

## 쿼리 매개변수

fake_items_db = [{'item_name': 'Foo'}, {'item_name': 'Bar'}, {'item_name': 'oo'}]

@app.get('/items/')
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]

from typing import Union

# 선택 매개변수

'''
@app.get('/items/{item_id}')
async def read_item(item_id: str, q: Union[str, None] = None, short : bool = False):
    
    item = {'item_id': item_id}

    if q:
        return {'item_id': item_id, 'q': q}
    
    if not short:
        item.update(
            {'description': 'This is an amazing item that has a long description'}
        )

    return item
'''

# 다중 경로 및 쿼리 매개변수, 필수 쿼리 매개변수

'''
@app.get('/items/{item_id}')
async def read_user_item(item_id: str, needy:str):
    item = {'item_id': item_id, 'needy': needy}
    return item
'''

@app.get('/items/{item_id}')
async def read_user_item(item_id:str, needy:str, skip:int=0, limit: Union[int,None] = None):
    item = {'item_id': item_id, 'needy': needy, 'skip': skip, 'limit': limit}
    return item

# http://127.0.0.1:8000/items/fooo?needy=hello&limit=3
