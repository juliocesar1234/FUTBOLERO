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


class nombre(BaseModel):
    nombre:str

    class Config:
        orm_mode = True