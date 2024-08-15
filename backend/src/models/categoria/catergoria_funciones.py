from sqlalchemy.orm import Session
from src.db import models

# PROCESOS QUE INTERACTUAN CON LA BASE DE DATOS
def crear_usario(cat,db:Session):
  nueva_categoria = models.cat_deport(**cat.model_dump())
  db.add(nueva_categoria)
  db.commit()
  db.refresh(nueva_categoria) 

def obtener_categoria(cat_id,db:Session):
    nueva_categoria = db.query(models.cat_deport).filter(models.cat_deport.id==cat_id).first()
    if not nueva_categoria:
        return {"Respuesta": "Categoria no encontrado!!"}
    return nueva_categoria

def eliminar_categoria(cat_id,db:Session):
    categoria = db.query(models.cat_deport).filter(models.cat_deport.id == cat_id)    
    if not categoria.first():
         return {"Respuesta": "Categoria no encontrado!!"}
    categoria.delete(synchronize_session=False)
    db.commit()
    return {"respuesta":"La categoria se ha eliminado"}

def obtener_categori_gr(db:Session):
    data = db.query(models.cat_deport).all()
    return data

def actualizar_categoria(cat_id,db:Session,updatecategoria):
    categoria = db.query(models.cat_deport).filter(models.cat_deport.id == cat_id) 
    if not categoria.first():
         return {"Respuesta": "Categoria no encontrado!!"}
    categoria.update(updatecategoria.dict(exclude_unset=True))
    db.commit()
    return {"Respuesta":"Categoria actualizada"}
