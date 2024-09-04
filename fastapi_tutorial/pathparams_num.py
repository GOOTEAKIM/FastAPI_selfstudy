from typing import Annotated, Union
from fastapi import FastAPI, Path, Query

app = FastAPI()

'''
@app.get('/items/{item_id}')
async def read_items(
    item_id: Annotated[int, Path(title='The ID of the item to get')], q: Annotated[Union[str, None], Query(alias='item-qurey')] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({'q':q})
    return results
'''

# 매개변수를 정렬하세요
'''
@app.get('/items/{item_id}')
async def read_items(
    q:str, item_id: Annotated[int, Path(title='The ID of the item to get')]
):
    results = {'item_id': item_id}
    if q:
        results.update({'q':q})
    return results
'''

# http://127.0.0.1:8000/items/3/?q=gootea

# 더 나은 Annotated

# ge : great than or equal
# gt : greater than
# le : less than or equal

'''
@app.get('/items/{item_id}')
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get", gt = 0, le = 1000)], q: str
):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    return results
'''

@app.get('/items/{item_id}')
async def read_items(
    *,
    item_id : Annotated[int, Path(title='The ID of the item to get', ge= 0, le = 1000 )],
    q: str, size : Annotated[float, Query(gt=0, lt=10.5)]
):
    results = {'item_id':item_id}
    if q:
        results.update({'q': q})
    if size:    
        results.update({'size': size})
    return results

# http://127.0.0.1:8000/items/123?q=example_query&size=9.5

