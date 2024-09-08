from src.db.database import Base
from sqlalchemy import Column,Integer,String


class Video_perfil(Base):

    __tablename__ = 'video_perfil'
    id = Column(Integer,primary_key = True,nullable = False,autoincrement=True)
    calidad = Column(String(30),nullable = False)
    ubicacion = Column(String(30),nullable = False)
    codigo_video = Column(Integer,nullable = False)
    estado = Column(Integer,nullable = False)