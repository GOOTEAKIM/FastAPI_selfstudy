from fastapi import APIRouter

from model.explorer import Explorer
import fake.explorer as service

# 파이썬 3.9에서는 | 연산자 못쓴다.
# 3.10 부터 가능하다.

from typing import Optional

router = APIRouter(prefix='/explorer')

@router.get('/')
def get_all() -> list[Explorer]:
    return service.get_all()

@router.get('/{name}')
def get_one(name) -> Optional[Explorer]:
    return service.get_one(name)

# 나머지 엔드 포인트. 현재는 아무 일도 하지 않는다.

@router.post('/')
def create(explorer:Explorer) -> Explorer:
    return service.create(explorer)

@router.patch('/{name}')
def modify(name, explorer:Explorer) -> Explorer:
    return service.modify(name,explorer)

@router.put('/{name}')
def replace(name, explorer:Explorer) -> Explorer:
    return service.replace(name, explorer)

@router.delete('/{name}')
def delete(name:str):
    return None