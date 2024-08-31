from src.db.database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.schema import ForeignKey
from datetime import datetime


class detalle_diciplina(Base):
    __tablename__ = "detalle_diciplina"
    id = Column(Integer, primary_key=True,autoincrement=True)
    respuesta = Column(String)
    fecha_registro = Column(DateTime,default=datetime.now,onupdate=datetime.now)
    estado = Column(Boolean,default=True)
    perfil_diciplina_id = Column(Integer, ForeignKey("perfil_diciplina.id",ondelete="CASCADE"))
    perfil_usuario_id = Column(Integer, ForeignKey("perfil_usuario.id",ondelete="CASCADE"))
    