from fastapi import APIRouter, Depends
from src.models.video_perfil.video_perfil_schema import Video_perfilData
from src.db.database import get_db
from sqlalchemy.orm import Session
from typing import List 
from src.models.video_perfil.video_perfil_models import Video_perfil


router_vidper = APIRouter(tags=["Video_perfils"])

#CREAR 
@router_vidper.post('/crear_video_perfils')
def crear_video_perfil(priv:Video_perfilData,db:Session = Depends(get_db)):
    nuevo_video_perfil = Video_perfil(**priv.model_dump())
    db.add(nuevo_video_perfil)
    db.commit()
    db.refresh(nuevo_video_perfil) 
    return {"Respuesta" : "Video Perfil creado satisfactoriamente"}

#CONSULTAR TODOS
@router_vidper.get('/obtener_video_perfil_todo', response_model=List[Video_perfilData])
def obtener_video_perfil_todo(db:Session = Depends(get_db)):
    data = db.query(Video_perfil).all()
    return data


#CONSULTAR POR ID
@router_vidper.get('/consultar_video_perfil_id/{vidper_id}',response_model=Video_perfilData)
def obtener_video_perfil(vidper_id:int,db:Session = Depends(get_db)):
    nueva_video_perfil = db.query(Video_perfil).filter(Video_perfil.id==vidper_id).first()
    if not nueva_video_perfil:
        return {"Respuesta": "Video Perfil no encontrado!!"}
    return nueva_video_perfil



#ELIMINAR POR EL ID
@router_vidper.delete('/eliminar_video_perfil/{vidper_id}')
def eliminar_video_perfil(vidper_id :int,db:Session = Depends(get_db)):

    Video_perfil = db.query(Video_perfil).filter(Video_perfil.id == vidper_id)    
    if not Video_perfil.first():
         return {"Respuesta": "Video Perfil no encontrado!!"}
    Video_perfil.delete(synchronize_session=False)
    db.commit()
    return {"respuesta":"El Video Perfil se ha eliminado"}


#ACTUALIZAR 
@router_vidper.patch('/actualizar_video_perfil/{vidper_id}')
def actualiza_video_perfil(vidper_id :int ,updatevidper:Video_perfilData,db:Session = Depends(get_db)):
   
    Video_perfil = db.query(Video_perfil).filter(Video_perfil.id == vidper_id) 
    if not Video_perfil.first():
         return {"Respuesta": "Video Perfil no encontrado!!"}
    Video_perfil.update(updatevidper.model_dump(exclude_unset=True))
    db.commit()
    return {"Respuesta":"Video Perfil actualizado"}