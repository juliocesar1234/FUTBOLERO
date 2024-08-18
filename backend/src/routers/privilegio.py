from fastapi import APIRouter, Depends
from src.models.privilegio.privilegio_schema import PrivilegioData
from src.db.database import get_db
from sqlalchemy.orm import Session
from typing import List 
from src.models.privilegio.privilegio_models import Privilegio


router_priv = APIRouter(tags=["Privilegios"])

#CREAR 
@router_priv.post('/crear_privilegios')
def crear_privilegio(priv:PrivilegioData,db:Session = Depends(get_db)):
    nuevo_privilegio = Privilegio(**priv.model_dump())
    db.add(nuevo_privilegio)
    db.commit()
    db.refresh(nuevo_privilegio) 
    return {"Respuesta" : "Categoria creado satisfactoriamente"}

#CONSULTAR TODOS
@router_priv.get('/obtener_privilegio_todo', response_model=List[PrivilegioData])
def obtener_privilegio_todo(db:Session = Depends(get_db)):
    data = db.query(Privilegio).all()
    return data


#CONSULTAR POR ID
@router_priv.get('/consultar_privilegio_id/{priv_id}',response_model=PrivilegioData)
def obtener_categoria(priv_id:int,db:Session = Depends(get_db)):
    nueva_privilegio = db.query(Privilegio).filter(Privilegio.id==priv_id).first()
    if not nueva_privilegio:
        return {"Respuesta": "Privilegio no encontrado!!"}
    return nueva_privilegio

#ELIMINAR POR EL ID
@router_priv.delete('/eliminar_privilegio/{priv_id}')
def eliminar_categoria(priv_id :int,db:Session = Depends(get_db)):

    privilegio = db.query(Privilegio).filter(Privilegio.id == priv_id)    
    if not privilegio.first():
         return {"Respuesta": "Privilegio no encontrado!!"}
    privilegio.delete(synchronize_session=False)
    db.commit()
    return {"respuesta":"El privilegio se ha eliminado"}


#ACTUALIZAR 
@router_priv.patch('/actualizar_privilegio/{priv_id}')
def actualiza_privilegio(priv_id :int ,updatepriv:PrivilegioData,db:Session = Depends(get_db)):
   
    privilegio = db.query(Privilegio).filter(Privilegio.id == priv_id) 
    if not privilegio.first():
         return {"Respuesta": "Privilegio no encontrado!!"}
    privilegio.update(updatepriv.model_dump(exclude_unset=True))
    db.commit()
    return {"Respuesta":"Privilegio actualizado"}

