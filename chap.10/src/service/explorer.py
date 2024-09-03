from model.explorer import Explorer

import fake.explorer as data

from typing import Optional

def get_all() -> list[Explorer]:
    return data.get_all()

def get_one(name:str) -> Optional[Explorer]:
    return data.get_one()

def create(explorer : Explorer) -> Explorer:
    return data.create(explorer)

def replace(name:str, explorer:Explorer) -> Explorer:
    return data.replace(name, explorer)

def modify(name:str, explorer:Explorer) -> Explorer:
    return data.modify(name,explorer)

def delete(name:str) -> bool:
    return data.delete(name)


