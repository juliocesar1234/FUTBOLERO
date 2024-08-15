from fastapi import FastAPI
from app.routers import categoriadeporte
from app.db.database import Base,engine


def create_tables():
    Base.metadata.create_all(bind=engine)
create_tables()

app = FastAPI()
app.include_router(categoriadeporte.router_cat)
# app.include_router(categoria_deporte.router, prefix ="/app/routers/categoria_deporte")
app.title = "FUTBOLERO"
app.version = "2.0"


# categoria_deporte = [
# {

#     "id": 1,
#     "nombre": "futbol",
#     "estado": True,
#     "descripcion": "Balones"

# },

# {

#     "id": 2,
#     "nombre": "futbolin",
#     "estado": True,
#     "descripcion": "Balon"

# }
# ]

# @app.get('/',tags=['Categoria Deporte'])
# def get_home():
#     return "hola mundo"

# @app.get('/categoria',tags=['Categoria Deporte'])
# def get_categoria():
#     return get_categoria

# @app.get('/categoria{id}',tags=['Categoria Deporte'])
# def get_categoria(id:int):
#     for categorias in categoria_deporte:
#         if categorias ['id'] == id:
#             return categorias
#     return []

# @app.get('/categoria/',tags=['Categoria Deporte'])
# def get_catdep(category: str, year: int ):
#     for categorias in categoria_deporte:
#         if categorias ['descripcion'] == category:
#             return categorias
#     return []

