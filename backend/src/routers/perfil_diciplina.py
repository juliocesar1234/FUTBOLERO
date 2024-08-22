from fastapi import APIRouter, Depends
from src.models.perfil_diciplina.perfil_diciplina_schemas import Perf_diciplina, UpdatePerfildic
from src.db.database import get_db
from sqlalchemy.orm import Session
from typing import List 
from src.models.perfil_diciplina import perfil_diciplina_funciones


router_perdic = APIRouter(tags=["Perfil_diciplina"])

#CREAR PERFIL DICIPLINA
@router_perdic.post('/perfil_diciplina')
def crear_diciplina(pdic:Perf_diciplina,db:Session = Depends(get_db)):
 perfil_diciplina_funciones.crear_perfil_diciplina(pdic,db) 
 return {"Respuesta" : "Perfil creado satisfactoriamente"}

#CONSULTAR TODOS
@router_perdic.get('/obtener_perfil_general', response_model=List[Perf_diciplina])
def obtener_perfildic_general(db:Session = Depends(get_db)):
   data = perfil_diciplina_funciones.obtener_perfil_diciplina_gr(db)
   return data

#CONSULTAR POR ID
@router_perdic.get('/perfil_buscar_id/{pedic}',response_model=Perf_diciplina)
def obtener_perfildic(pedic:int,db:Session = Depends(get_db)):
    nueva_categoria = perfil_diciplina_funciones.obtener_perfil_diciplina(pedic,db)
    return nueva_categoria

#ELIMINAR POR EL ID
@router_perdic.delete('/perfil_delet/{pedic}')
def eliminar_perfildic(pedic :int,db:Session = Depends(get_db)):
    res =perfil_diciplina_funciones.eliminar_perfil_diciplina(pedic,db)
    return res


#ACTUALIZAR 
@router_perdic.patch('/perfil_actualizar/{pedic}')
def actualizar_perfildic(pedic :int ,updateperfildic:UpdatePerfildic,db:Session = Depends(get_db)):
   act = perfil_diciplina_funciones.actualizar_perfil_diciplina(pedic,db,updateperfildic)
   return act
