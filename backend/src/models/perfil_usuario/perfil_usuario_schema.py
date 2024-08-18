from pydantic import BaseModel
from sqlalchemy import DECIMAL


class Perfil_usuarioData(BaseModel):
    nombre: str
    apellido : str
    pais : str
    ciudad : str
    peso : float
    estatura : float
    edad : int
    telefono : int
    id_usuario : int
    estado: int


class UpdatePerfil_usuario(BaseModel): #Actualiza
    nombre: str = None
    apellido : str= None
    pais: str =None
    ciudad: str =None
    peso: float =None
    estatura: float =None
    edad: int =None
    telefono: int =None
    id_usuario: int =None
    estado: int =None
    

class ShowPerfil_usuario(BaseModel):
    nombre: str
    apellido : str
    pais: str 
    ciudad: str 
    peso: float 
    estatura: float 
    edad: int 
    telefono: int 
    id_usuario: int 
    estado: int 
    class Config():
        orm_mode = True