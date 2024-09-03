from fastapi import FastAPI
from pydantic import BaseModel

from typing import Union

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

app = FastAPI()

# 모델을 사용하세요

@app.post('/items/')
async def create_item(item: Item):
    item_dict = item.dict()

    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({'price_with_tax': price_with_tax})
    return item_dict

# 요청 본문 + 경로 매개변수

'''
@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item):
    return {'item_id': item_id, **item.dict()}
'''

# 요청 본문 + 경로 + 쿼리 매개변수

@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item, q : Union[str, None] = None):
    result = {'item_id': item_id, **item.dict()}
    if q:
        result.update({"q":q})
    return result