from typing import Annotated, Union

from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name:str
    description: Union[str, None]=Field(
        default=None, title='The description of the item', max_length=300
    )
    price: float = Field(gt=0, description='The price must be greater than zero')
    tax: Union[float, None] = None

@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {'item_id':item_id, 'item': item}
    return results

# http://127.0.0.1:8000/items/100

'''json
{
    "item" : {
        "name": "kim",
        "price": 30.2
    }

}
'''

