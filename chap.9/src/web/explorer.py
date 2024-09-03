from fastapi import APIRouter
from model.explorer import Explorer
import service.explorer as service

from typing import Optional

router = APIRouter(prefix="/explorer")

@router.get('/')
def get_all() -> list[Explorer]:
    return service.get_all()

@router.get('/{name}')
def get_one(name) -> Optional[Explorer]:
    return service.get_one()

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