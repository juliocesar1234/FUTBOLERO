from fastapi import FastAPI
from src.routers import categoriadeporte
from src.routers import privilegio
from src.db.database import Base,engine


def create_tables():
    Base.metadata.create_all(bind=engine)
create_tables()

app = FastAPI()
app.include_router(categoriadeporte.router_cat)
app.include_router(privilegio.router_priv)
# app.include_router(categoria_deporte.router, prefix ="/app/routers/categoria_deporte")
app.title = "FUTBOLERO"
app.version = "2.0"

