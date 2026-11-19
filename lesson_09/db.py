from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.engine import URL

connection_url = URL.create(
    drivername="postgresql+psycopg",
    username="postgres",
    password="4334",  
    host="localhost",
    port=5432,
    database="postgres"
)

engine = create_engine(connection_url, echo=False)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()
