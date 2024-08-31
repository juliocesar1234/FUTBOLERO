from fastapi import APIRouter, Depends
from src.models.detalle_diciplina.detalle_diciplina_schemas import Updatedetallediciplina, Showdetalldiciplina
from src.db.database import get_db
from sqlalchemy.orm import Session
from typing import List 
from src.models.detalle_diciplina.detalle_diciplina_models import detalle_diciplina


router_detalldic = APIRouter(tags=["Detalle_diciplina"])

#CREAR 
@router_detalldic.post('/crear_detalle_diciplina')
def crear_detalle_diciplina(dedic:Showdetalldiciplina,db:Session = Depends(get_db)):
    nuevo_detalle_perfil = detalle_diciplina(**dedic.model_dump())
    db.add(nuevo_detalle_perfil)
    db.commit()
    db.refresh(nuevo_detalle_perfil) 
    return {"Respuesta" : "Detalle perfil creado satisfactoriamente"}

#CONSULTAR TODOS
@router_detalldic.get('/obtener_detalle_diciplina', response_model=List[Showdetalldiciplina])
def obtener_detalle_diciplina_todo(db:Session = Depends(get_db)):
    data = db.query(detalle_diciplina).all()
    return data


#CONSULTAR POR ID
@router_detalldic.get('/consultar_detalle_diciplina/{dedic_id}',response_model=Showdetalldiciplina)
def obtener_detalle_perfil(dedic_id:int,db:Session = Depends(get_db)):
    nueva_detalle_perfil = db.query(detalle_diciplina).filter(detalle_diciplina.id==dedic_id).first()
    if not nueva_detalle_perfil: 
     return {'Respuesta': 'Detalle perfil no encontrado!!'}
    return nueva_detalle_perfil

#ELIMINAR POR EL ID
@router_detalldic.delete('/eliminar_detalle_diciplina/{dedic_id}')
def eliminar_detalle_diciplina(dedic_id :int,db:Session = Depends(get_db)):
    Detalldic = db.query(detalle_diciplina).filter(detalle_diciplina.id == dedic_id)    
    if not Detalldic.first():
         return {"Respuesta": "Detalle diciplina no encontrado!!"}
    Detalldic.delete(synchronize_session=False)
    db.commit()
    return {"respuesta":"El detalle diciplina se ha eliminado"}


#ACTUALIZAR 
@router_detalldic.patch('/actualizar_detalle_diciplina/{dedic_id}')
def actualiza_detalle_diciplina(dedic_id :int ,updatdedic:Updatedetallediciplina,db:Session = Depends(get_db)):
    detalle_diciplinac = db.query(detalle_diciplina).filter(detalle_diciplina.id == dedic_id) 
    if not detalle_diciplinac.first():
         return {"Respuesta": "Detalle diciplina no encontrado!!"}
    detalle_diciplinac.update(updatdedic.model_dump(exclude_unset=True))
    db.commit()
    return {"Respuesta":"Detalle diciplina actualizado"}