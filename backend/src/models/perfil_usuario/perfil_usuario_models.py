from src.db.database import Base
from sqlalchemy import Column,Integer,String,DECIMAL,FLOAT


class Perfil_usuario(Base):

    __tablename__ = 'perfil_usuario'
    id = Column(Integer,primary_key = True,nullable = False,autoincrement=True)
    nombre = Column(String(30),nullable = False)
    apellido = Column(String(30),nullable = False)
    pais = Column(String(30),nullable = False)
    ciudad = Column(String(30),nullable = False)
    peso = Column(FLOAT,nullable = False)
    estatura = Column(FLOAT,nullable = False)
    edad = Column(Integer,nullable = False)
    telefono = Column(Integer,nullable = False)
    id_usuario = Column(Integer,nullable = False)
    estado = Column(Integer,nullable = False)