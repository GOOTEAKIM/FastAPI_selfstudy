from fastapi import FastAPI, HTTPException, Request, status

from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.encoders import jsonable_encoder

from pydantic import BaseModel

from fastapi.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler
)

class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name

app = FastAPI()

items = {'foo' : 'The Foo wrestlers'}

'''
@app.get('/items/{item_id}')
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail='Item not found',
                            headers={"X-Error": 'There goes my error'})
    return {'item':items[item_id]}

'''

@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request:Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."}
    )

@app.get('/unicorns/{name}')
async def read_unicorn(name:str):
    if name == 'yolo':
        raise UnicornException(name = name)
    
# @app.exception_handler(StarletteHTTPException)
# async def http_exception_handler(request, exc):
#     return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    print(f"OMG! An HTTP error! : {repr(exc)}")
    return await http_exception_handler(request, exc)

# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request: Request, exc: RequestValidationError):
#     return JSONResponse(
#         status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
#         content=jsonable_encoder({'detail': exc.errors(), 'body': exc.body})
#     )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request,exc):
    print(f"OMG! The client sent invalid data! : {exc}")
    return await request_validation_exception_handler(request, exc)

class Item(BaseModel):
    title: str
    size: int

@app.get('/items/{item_id}')
async def read_item(item_id:int):
    if item_id == 3:
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
    return {'item_id': item_id}

@app.post('/items/')
async def create_item(item: Item):
    return item