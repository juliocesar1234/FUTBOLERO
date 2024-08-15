from src.db.database import Base
from sqlalchemy import Column, Integer, String, Boolean,DateTime
from datetime import datetime

class cat_deport(Base):
    __tablename__ = "Categoria_Deporte"
    id = Column(Integer, primary_key=True,autoincrement=True)
    nombre = Column(String,unique=True)
    descripcion = Column(String)
    observacion= Column(String)
    registro = Column(DateTime,default=datetime.now,onupdate=datetime.now)
    estado= Column(Boolean,default=True)

