from sqlalchemy.orm import Session
from .models import Item

def get_functionality_items(db: Session):
    return db.query(Item.supplementSeq, Item.supplementName, Item.supplementDiscription, Item.functionality).all()
