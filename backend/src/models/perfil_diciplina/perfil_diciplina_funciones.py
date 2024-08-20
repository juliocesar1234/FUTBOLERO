from sqlalchemy.orm import Session
from src.models.perfil_diciplina.perfil_diciplina_models import perfil_diciplina

#CREAR DICIPLIA
def crear_perfil_diciplina(pdic,db:Session):
  nuevo_perfil = perfil_diciplina(**pdic.model_dump())
  db.add(nuevo_perfil)
  db.commit()
  db.refresh(nuevo_perfil) 

def obtener_perfil_diciplina(pedic,db:Session):
    nuevo_perfildiciplina = db.query(perfil_diciplina).filter(perfil_diciplina.id==pedic).first()
    if not nuevo_perfildiciplina:
        return {"Respuesta": "Perfil diciplina no encontrado!!"}
    return nuevo_perfildiciplina

def eliminar_perfil_diciplina(pedic,db:Session):
    perfildic = db.query(perfil_diciplina).filter(perfil_diciplina.id == pedic)    
    if not perfildic.first():
         return {"Respuesta": "Perfil diciplina no encontrado!!"}
    perfildic.delete(synchronize_session=False)
    db.commit()
    return {"respuesta":"El perfil diciplina se ha eliminado"}

def obtener_perfil_diciplina_gr(db:Session):
    data = db.query(perfil_diciplina).all()
    return data

def actualizar_perfil_diciplina(pedic,db:Session,updateperfildic):
    perfildic = db.query(perfil_diciplina).filter(perfil_diciplina.id == pedic) 
    if not perfildic.first():
         return {"Respuesta": "El perfil diciplina no encontrado!!"}
    perfildic.update(updateperfildic.dict(exclude_unset=True))
    db.commit()
    return {"Respuesta":"Perfil diciplina actualizada"}