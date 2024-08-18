from src.db.database import Base
from sqlalchemy import Column, Integer, String, Boolean,DateTime
from datetime import datetime
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship

class cat_deport(Base):
    __tablename__ = "Categoria_Deporte"
    id = Column(Integer, primary_key=True,autoincrement=True)
    nombre = Column(String,unique=True)
    descripcion = Column(String)
    observacion= Column(String)
    registro = Column(DateTime,default=datetime.now,onupdate=datetime.now)
    estado= Column(Boolean,default=True)
    # diciplina = relationship("Perfil_Diciplina",backref="Categoria_Deporte",cascade="delete,merge")


class perfil_diciplina(Base):
    __tablename__ = "Perfil_Diciplina"
    id = Column(Integer, primary_key=True,autoincrement=True)
    categoria_id = Column(Integer, ForeignKey("Categoria_Deporte.id",ondelete="CASCADE"))
    diciplina = Column(Integer)
    nombre_titulo = Column(String,unique=True)
    estado= Column(Boolean,default=True)