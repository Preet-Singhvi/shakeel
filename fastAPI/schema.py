# build a schema using pydantic
from pydantic import BaseModel
from geoalchemy2 import Geometry
class Pole(BaseModel):
    pole_id: str
    linear_id: str
    latitude: float
    longitude: float
    side: str
    pole_type:str
    point:Geometry

    class Config:
        orm_mode = True

