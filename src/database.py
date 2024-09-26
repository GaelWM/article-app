from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

user= os.getenv('POSTGRES_USER', 'postgres')
password= os.getenv('POSTGRES_PASSWORD', 'password')
host= os.getenv('POSTGRES_HOST', 'localhost')
port= os.getenv('POSTGRES_PORT', '5432')
database= os.getenv('POSTGRES_DB', 'fastapi_db')

DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{database}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
