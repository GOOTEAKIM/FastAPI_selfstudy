from model.creature import Creature
from service import cre as code
sample = Creature(
    name='Yeti',
    country='CN',
    area='Himalayas',
    description='Hirsute Himalayan',
    aka='Abominable Snowman'
)


def test_create():
    resp = code.create(sample)
    assert resp == sample

def test_get_exists():
    resp = code.get_one('Yeti')