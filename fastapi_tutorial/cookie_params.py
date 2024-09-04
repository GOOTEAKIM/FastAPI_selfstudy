from typing import Union, Annotated

from fastapi import FastAPI, Cookie

app = FastAPI()

@app.get('/items/')
async def read_items(ads_id: Annotated[Union[str, None], Cookie()] = None):
    return {'ads_id':ads_id}

# http://127.0.0.1:8000/items/

# Headers에 Cookie : ads_id=12345 이렇게 넣어야 한다.