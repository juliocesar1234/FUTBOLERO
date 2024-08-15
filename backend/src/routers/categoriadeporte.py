from fastapi import APIRouter, Depends
from backend.src.models.categoria.categoria_schemas import ShowCat,UpdateCategoria
from src.db.database import get_db
from sqlalchemy.orm import Session
from typing import List 
from src.models.categoria import catergoria_funciones

router_cat = APIRouter(tags=["Caterogoria Deporte"])

#CREAR 
@router_cat.post('/crear_categoria')
def crear_categoria(cat:ShowCat,db:Session = Depends(get_db)):
 catergoria_funciones.crear_usario(cat,db) 
 return {"Respuesta" : "Categoria creado satisfactoriamente"}

#CONSULTAR TODOS
@router_cat.get('/obtener_categoria_general', response_model=List[ShowCat])
def obtener_categoria_general(db:Session = Depends(get_db)):
   data = catergoria_funciones.obtener_categori_gr(db)
   return data

#CONSULTAR POR ID
@router_cat.get('/categoria/{cat_id}',response_model=ShowCat)
def obtener_categoria(cat_id:int,db:Session = Depends(get_db)):
    nueva_categoria = catergoria_funciones.obtener_categoria(cat_id,db)
    return nueva_categoria

#ELIMINAR POR EL ID
@router_cat.delete('/categoria_delet/{cat_id}')
def eliminar_categoria(cat_id :int,db:Session = Depends(get_db)):
    res =catergoria_funciones.eliminar_categoria(cat_id,db)
    return res


#ACTUALIZAR 
@router_cat.patch('/categoria_actualizar/{cat_id}')
def actualiza_categorias(cat_id :int ,updatecategoria:UpdateCategoria,db:Session = Depends(get_db)):
   act = catergoria_funciones.actualizar_categoria(cat_id,db,updatecategoria)
   return act

