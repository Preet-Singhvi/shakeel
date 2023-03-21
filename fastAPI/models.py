from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base  = declarative_base()

class Pole(Base):
    __tablename__ = 'pole'
    pole_id  = Column(String, primary_key=True, index=True)
    linear_id = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    side = Column(String)
    pole_type = Column(String)
    point = Column()





