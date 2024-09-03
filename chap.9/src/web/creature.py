from fastapi import APIRouter

from model.creature import Creature
import service.creature as service

from typing import Optional

router = APIRouter(prefix= '/creature')

@router.get('/')
def get_all() -> list[Creature]:
    return service.get_all()

@router.get('/{name}')
def get_one(name) -> Creature:
    return service.get_one()

@router.post('/')
def create(creature:Creature) -> Creature:
    return service.create(creature)

@router.patch('/{name}')
def modify(name, creature: Creature) -> Creature:
    return service.modify(name,creature)

@router.put('/{name}')
def replace(name, creature:Creature) -> Creature:
    return service.replace(name,creature)

@router.delete('/{name}')
def delete(name:str):
    return service.delete(name)