# 9/3

## FastAPI

### 설치

- pip install fastapi
- pip install uvicorn

### 예제

#### 만들기

- main.py 파일을 생성한다.

```python
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

#### 실행하기

- uvicorn main:app --reload

#### 확인하기

- http://127.0.0.1:8000/items/5?q=somequery

- postman으로 실행 시
  - http://127.0.0.1:8000/items/
  - Params : q : app(예시)

#### 대화형 API 문서

- http://127.0.0.1:8000/docs

#### 대안 API 문서

- http://127.0.0.1:8000/redoc

### 예제 심화

```python
from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name:str
    price:float
    is_offer: Union[bool,None] = None

@app.get('/')
def read_rood():
    return {"hello": "world"}

@app.get('/items/{item_id}')
def read_item(item_id: int, q: Union[str,None] = None):
    return {"item_id": item_id, "q":q}

@app.put('/items/{item_id}')
def update_item(item_id:int, item: Item):
    return {"item_name" : item.name, "item_id": item_id}
```

- http://127.0.0.1:8000/docs 로 이동
- Try it out > Request Body 수정 후 Execute > 매개변수 전송

## 기능

