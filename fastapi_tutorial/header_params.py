from typing import Annotated, Union, List
from fastapi import FastAPI, Header

app = FastAPI()

# Header 매개 변수 선언
'''
@app.get('/items/')
async def read_items(user_agent: Annotated[Union[str,None], Header()] = None):
    return {'User-Agent': user_agent}
'''

# 자동 변환
'''
@app.get('/items/')
async def read_items(strange_header : Annotated[
    Union[str,None], Header(convert_underscores=False)
] = None,):
    return {'strange_header': strange_header}
'''

# 중복된 헤더

@app.get('/items/')
async def read_items(x_token: Annotated[Union[List[str], None], Header()] = None):
    return {'X-Token values': x_token} 
