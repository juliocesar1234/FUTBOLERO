from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:casar007@localhost:5432/postgres"
#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:@localhost:5432/futbolero"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Passw0rd@localhost:5432/postgres"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal= sessionmaker( bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def  get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()