from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

'''
class Item(BaseModel):
    name:str
    description: Union[str,None]= None
    price: float
    tax: Union[float, None]=None

    # 리스트 일때
    # tags: list[str] =[]
    # tags: list= []

    # 유형 설정 : 태그는 고유한 문자열이다. > set 사용
    tags: set[str] = set()
'''

# 중첩 모델

# 하위 모델 정의

class Image(BaseModel):
    # url:str
    url:HttpUrl
    name:str

class Item(BaseModel):
    name:str
    description: Union[str,None]= None
    price: float
    tax: Union[float,None]=None
    tags: set[str] = set()
    images: Union[list[Image], None]= None

class Offer(BaseModel):
    name:str
    description: Union[str, None] = None
    price:float
    items:list[Item]

@app.put('/items/{item_id}')
async def update_item(item_id:int, item:Item):
    results = {'item_id': item_id, 'item': item}
    return results


'''json
{
    "name": "goo",
    "price":3.1,
    "tags": ["1", "2"]
}
'''

'''json
tags 가 set 이면 중복 된 것을 없애고 출력한다. 

{
    "name": "goo",
    "price":3.1,
    "tags": ["kim", "goo", "goo","goo"]
}
'''

'''json
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2,
    "tags": [
        "rock",
        "metal",
        "bar"
    ],
    "images": [
        {
            "url": "http://example.com/baz.jpg",
            "name": "The Foo live"
        },
        {
            "url": "http://example.com/dave.jpg",
            "name": "The Baz"
        }
    ]
}   
'''

@app.post('/offers/')
async def create_offer(offer: Offer):
    return offer

'''json
{
    "name": "Special Offer",
    "description": "A special discount on selected items",
    "price": 99.99,
    "items": [
        {
            "name": "Item1",
            "description": "The first item",
            "price": 50.0,
            "tax": 5.0,
            "tags": ["tag1", "tag2"],
            "images": [
                {
                    "url": "http://example.com/item1.jpg",
                    "name": "Item 1 image"
                }
            ]
        },
        {
            "name": "Item2",
            "description": "The second item",
            "price": 30.0,
            "tax": 3.0,
            "tags": ["tag3", "tag4"],
            "images": [
                {
                    "url": "http://example.com/item2.jpg",
                    "name": "Item 2 image"
                }
            ]
        }
    ]
}

'''

@app.post('/images/multiple/')
async def create_multiple_images(images: list[Image]):
    return images

'''json
[
    {
        "url": "http://example.com/image1.jpg",
        "name": "Image 1"
    },
    {
        "url": "http://example.com/image2.jpg",
        "name": "Image 2"
    },
    {
        "url": "http://example.com/image3.jpg",
        "name": "Image 3"
    }
]

'''

@app.post('/index-weights/')
async def create_index_weights(weights:dict[int,float]):
    return weights

'''json
{
    "3":3.4,
    "2":2.6
}
'''