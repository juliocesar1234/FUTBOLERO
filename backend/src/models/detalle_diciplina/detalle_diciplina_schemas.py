from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Updatedetallediciplina(BaseModel): #Actualiza
    respuesta: str = None
    perfil_diciplina_id: int = None
    perfil_usuario_id: int = None
    estado : int = None
    

class Showdetalldiciplina(BaseModel):
    respuesta: str
    perfil_diciplina_id: int
    perfil_usuario_id: int 
    estado: int
    class Config():
        orm_mode = True

class clasedic(BaseModel): #Actualiza
    respuesta: str 
    perfil_diciplina_id: int 
    perfil_usuario_id: int 
    estado : int 