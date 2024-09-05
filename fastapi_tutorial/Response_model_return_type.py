from typing import Union, Any, List

from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse, RedirectResponse
from pydantic import BaseModel, EmailStr

app = FastAPI()

class Item(BaseModel):
    name:str
    description: Union[str,None] = None
    price: float
    tax: float = 10.5

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The Bar fighters", "price": 62, "tax": 20.2},
    "baz": {
        "name": "Baz",
        "description": "There goes my baz",
        "price": 50.2,
        "tax": 10.5,
    },
}

class BaseUser(BaseModel):
    username:str
    email:EmailStr
    full_name: Union[str,None]=None

class UserOut(BaseModel):
    username:str
    email:EmailStr
    full_name: Union[str, None]=None

class UserIn(BaseModel):
    password: str

@app.post('/items/', response_model=Item)
async def create_item(item: Item) -> Any:
    return item

@app.get('/items/', response_model=list[Item])
async def read_items() -> Any:
    return [
        Item(name='Portal Gun', price=42.0),
        Item(name='Plumbus', price=32.0),
    ]

# @app.post("/user/")
# async def create_user(user: UserIn) -> UserIn:
#     return user

'''json
{
    "username":"kim",
    "password":"kim123",
    "email":"gootae0220@naver.com"
}
'''

# @app.post('/user/', response_model=UserOut)
# async def create_user(user:UserIn) -> Any:
#     return user

@app.post('/user/')
async def create_user(user:UserIn) ->BaseModel:
    return user

# @app.get('/portal')
# async def get_portal(teleport: bool = False) -> Response:
#     if teleport:
#         return RedirectResponse(url='https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    
#     return JSONResponse(content={"message": "Here's your interdimensional portal."})

@app.get("/portal", response_model=None)  # response_model을 None으로 설정
async def get_portal(teleport: bool = False) -> Union[Response, dict]:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return {"message": "Here's your interdimensional portal."}

@app.get('/teleport')
async def get_teleport() -> RedirectResponse:
    return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")

@app.get('/items/{item_id}', response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]

@app.get('/items/{item_id}/name', response_model=Item, response_model_include=['name', 'description'],)
async def read_item_name(item_id:str):
    return items[item_id]

@app.get('/items/{item_id}/public', response_model=Item, response_model_exclude={"tax"})
async def read_item_public_data(item_id:str):
    return items[item_id]