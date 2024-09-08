from pydantic import BaseModel


class Video_perfilData(BaseModel):
    calidad: str
    ubicacion : str
    codigo_video : int
    estado: int


class UpdateVideo_perfil(BaseModel): #Actualiza
    calidad: str = None
    ubicacion : str= None
    codigo_video: int =None
    estado: int =None
    

class ShowVideo_perfil(BaseModel):
    calidad: str
    ubicacion : str
    codigo_video: int 
    estado: int 
    class Config():
        orm_mode = True