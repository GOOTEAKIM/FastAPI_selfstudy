from typing import Union, Any

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class Item(BaseModel):
    name:str
    description: Union[str,None] = None
    price: float
    tax: Union[float,None] = None
    tags: list[str] = []

class UserIn(BaseModel):
    username:str
    password: str
    email:EmailStr
    full_name: Union[str, None]=None

@app.post('/items/', response_model=Item)
async def create_item(item: Item) -> Any:
    return item

@app.get('/items/', response_model=list[Item])
async def read_items() -> Any:
    return [
        Item(name='Portal Gun', price=42.0),
        Item(name='Plumbus', price=32.0),
    ]

@app.post("/user/")
async def create_user(user: UserIn) -> UserIn:
    return user

'''json
{
    "username":"kim",
    "password":"kim123",
    "email":"gootae0220@naver.com"
}
'''

# 동일한 입력 데이터를 반환합니다.
