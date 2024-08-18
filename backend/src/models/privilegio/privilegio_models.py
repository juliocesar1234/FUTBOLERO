from src.db.database import Base
from sqlalchemy import Column,Integer,String


class Privilegio(Base):

    __tablename__ = 'privilegio'
    id = Column(Integer,primary_key = True,nullable = False,autoincrement=True)
    nombre = Column(String(30),nullable = False)
    estado = Column(Integer,nullable = False)