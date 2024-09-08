from sqlalchemy import Column, Integer, String
from .database import Base

class Item(Base):
    __tablename__ = 'items'
    
    supplementSeq = Column(Integer, primary_key=True, index=True)
    supplementName = Column(String, index=True)
    supplementDiscription = Column(String)
    functionality = Column(String, index=True)
