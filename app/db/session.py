from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./shop.db"  # Local SQLite file

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}  # Required only for SQLite
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()