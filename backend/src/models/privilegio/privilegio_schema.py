from pydantic import BaseModel


class PrivilegioData(BaseModel):
    nombre: str
    estado: int


    class Config:
        orm_mode = True


class PrivilegioId(PrivilegioData):
    id: int

    class Config:
        orm_mode = True


class PrivilegioDataActualiza(BaseModel):
    nombre:str = None
    estado:int = None

    class Config:
        orm_mode = True