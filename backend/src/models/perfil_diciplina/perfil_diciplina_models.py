from src.db.database import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.schema import ForeignKey


class perfil_diciplina(Base):
    __tablename__ = "perfil_diciplina"
    id = Column(Integer, primary_key=True,autoincrement=True)
    categoria_id = Column(Integer, ForeignKey("Categoria_Deporte.id",ondelete="CASCADE"))
    html_select = Column(String)
    nombre_titulo = Column(String)
    estado= Column(Boolean,default=True)