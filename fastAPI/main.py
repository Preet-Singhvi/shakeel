import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from schema import Pole as SchemaPole
from schema import Pole
from models import Pole as ModelPole
import os
from dotenv import load_dotenv

load_dotenv('.env')


app = FastAPI()

# to avoid csrftokenError
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

@app.get("/")
async def root():
    return {"message": "hello world"}


@app.post('/pole/', response_model=SchemaPole)
async def pole(pole: SchemaPole):
    db_pole = ModelPole(pole_id=pole.pole_id,linear_id=pole.linear_id,latitude=pole.latitude,longitude=pole.longitude,side=pole.side,pole_type=pole.pole_type,geometry=(str(pole.latitude),str(pole.longitude)))
    #geometry=str(pole.latitude,pole.longitude)
    db.session.add(db_pole)
    db.session.commit()
    return db_pole

@app.get('/pole/')
async def pole():
    pole = db.session.query(ModelPole).all()
    return pole

@app.put('/pole/', response_model=SchemaPole)
async def pole(pole_id:int ,pole: SchemaPole):
    db_pole = ModelPole(pole_id=pole.pole_id,linear_id=pole.linear_id,latitude=pole.latitude,longitude=pole.longitude,side=pole.side,pole_type=pole.pole_type,geometry=(str(pole.latitude),str(pole.longitude)))
    #pole.geometry=str(pole.latitude,pole.longitude)
    pole = db.session.query(ModelPole).all()
    for i in pole:
        if i.pole_id==pole_id:
            db.session.delete(i)
            db.session.commit()
    db.session.add(db_pole)
    db.session.commit()
    return db_pole

# @app.put("/pole/{pole_id}",response_model=SchemaPole)
# async def update_pole(pole_id: int, pole: SchemaPole):
#     for i in pole:
#         if i.pole_id == pole_id:
#             db_pole = ModelPole(pole_id=pole.pole_id,linear_id=pole.linear_id,latitude=pole.latitude,longitude=pole.longitude,side=pole.side,pole_type=pole.pole_type)
#             pole[i] = pole.dict()
#             return {"message": "Pole updated successfully"}
#     # return {"error": "Pole not found"}


@app.delete("/pole")
async def delete_pole(pole_id: int):
    pole = db.session.query(ModelPole).all()
    for i in pole:
        if i.pole_id==pole_id:
            db.session.delete(i)
            db.session.commit()
            print(i)
            print(pole)
        
        # if i["pole_id"]== pole_id:
        #     del pole[i]
        return {"message": "Pole deleted successfully"}
    return {"error": "Pole not found"}
    


# To run locally
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)