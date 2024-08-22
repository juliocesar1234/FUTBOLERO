from fastapi import APIRouter, Depends
from src.models.perfil_usuario.perfil_usuario_schema import Perfil_usuarioData
from src.db.database import get_db
from sqlalchemy.orm import Session
from typing import List 
from src.models.perfil_usuario.perfil_usuario_models import Perfil_usuario


router_perusu = APIRouter(tags=["Perfil_usuarios"])

#CREAR 
@router_perusu.post('/crear_perfil_usuarios')
def crear_perfil_usuario(priv:Perfil_usuarioData,db:Session = Depends(get_db)):
    nuevo_perfil_usuario = Perfil_usuario(**priv.model_dump())
    db.add(nuevo_perfil_usuario)
    db.commit()
    db.refresh(nuevo_perfil_usuario) 
    return {"Respuesta" : "Perfil Usuario creado satisfactoriamente"}

#CONSULTAR TODOS
@router_perusu.get('/obtener_perfil_usuario_todo', response_model=List[Perfil_usuarioData])
def obtener_perfil_usuario_todo(db:Session = Depends(get_db)):
    data = db.query(Perfil_usuario).all()
    return data


#CONSULTAR POR ID
@router_perusu.get('/consultar_perfil_usuario_id/{perusu_id}',response_model=Perfil_usuarioData)
def obtener_perfil_usuario(perusu_id:int,db:Session = Depends(get_db)):
    nueva_perfil_usuario = db.query(Perfil_usuario).filter(Perfil_usuario.id==perusu_id).first()
    if not nueva_perfil_usuario:
        return {"Respuesta": "Perfil Usuario no encontrado!!"}
    return nueva_perfil_usuario

#ELIMINAR POR EL ID
@router_perusu.delete('/eliminar_perfil_usuario/{perusu_id}')
def eliminar_perfil_usuario(perusu_id :int,db:Session = Depends(get_db)):

    Perfil_usuario = db.query(Perfil_usuario).filter(Perfil_usuario.id == perusu_id)    
    if not Perfil_usuario.first():
         return {"Respuesta": "Perfil Usuario no encontrado!!"}
    Perfil_usuario.delete(synchronize_session=False)
    db.commit()
    return {"respuesta":"El Perfil Usuario se ha eliminado"}


#ACTUALIZAR 
@router_perusu.patch('/actualizar_perfil_usuario/{perusu_id}')
def actualiza_perfil_usuario(perusu_id :int ,updateperusu:Perfil_usuarioData,db:Session = Depends(get_db)):
   
    Perfil_usuario = db.query(Perfil_usuario).filter(Perfil_usuario.id == perusu_id) 
    if not Perfil_usuario.first():
         return {"Respuesta": "Perfil Usuario no encontrado!!"}
    Perfil_usuario.update(updateperusu.model_dump(exclude_unset=True))
    db.commit()
    return {"Respuesta":"Perfil Usuario actualizado"}