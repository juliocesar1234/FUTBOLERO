from pydantic import BaseModel


class Perf_diciplina(BaseModel):
    categoria_id :int
    html_select : str
    nombre_titulo: str
    estado : int
    class Config():
        orm_mode = True

class UpdatePerfildic(BaseModel): #Actualiza
    categoria_id :int = None
    html_select : str = None
    nombre_titulo: str = None
    estado : int = None
   
    