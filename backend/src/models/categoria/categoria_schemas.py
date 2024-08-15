from pydantic import BaseModel
from typing import Optional
from datetime import datetime

#cat Model
class categoria_deporte1(BaseModel): #Schema

    nombre: str
    descripcion : str
    observacion: Optional[str]
    registro: datetime = datetime.now()
    #estado: 

class UpdateCategoria(BaseModel): #Actualiza
    nombre: str = None
    descripcion : str= None
    observacion: str =None
    


class ShowCat(BaseModel):
    nombre: str
    descripcion: str
    observacion: str
    
    class Config():
        orm_mode = True