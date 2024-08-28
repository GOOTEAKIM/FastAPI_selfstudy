from model.creature import Creature

# 가짜 데이터 . 10장에서 실제 데이터베이스와 SQL 로 바꾼다

from typing import Optional

_creatures = [
    Creature(name='Yeti',
             aka='Abominable Snowman',
             country='CN',
             area='Himalayas',
             description='Hirsute Himalayan'),

    Creature(name='Bigfoot',
            description='Hirsute Himalayan',
            country='US',
            area='*',
            aka="Sasquatch"
            ),
]

def get_all() -> list[Creature]:
    # 생명체 목록을 반환
    return _creatures

def get_one(name:str) -> Optional[Creature]:
    # 검색한 생명체 반환

    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    return None

# 다음 함수는 현재 올바로 동작하지 않는다
# 실제로는 _explorers 목록을 수정하지 않지만,
# 마치 작동하는 것처럼 동작한다.

def create(creature: Creature) -> Creature:
    # 생명체 추가
    return creature

def modify(name:str, creature: Creature) -> Creature:
    # 생명체 정보 일부를 수정
    return creature

def replace(name:str, creature: Creature) -> Creature:
    # 생명체를 완전히 교체
    return creature

def delete(name:str) -> bool:
    # 생명체를 삭제, 만약에 대상이 없다면 False 반환

    for _creature in _creatures:
        if _creature.name == name:
            return True
    
    return False
