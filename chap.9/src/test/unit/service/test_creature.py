from model.creature import Creature
from service import create, get_all, get_one, replace, modify, delete

sample = Creature(
    name='Yeti',
    country='CN',
    area='Himalayas',
    description='Hirsute Himalayan',
    aka='Abominable Snowman'
)

def test_create():
    resp = create(sample)
    assert resp == sample

def test_get_exists():
    resp = get_one('Yeti')
    assert resp == sample

def test_get_missing():
    resp = get_one('boxturtle')
    assert resp is None