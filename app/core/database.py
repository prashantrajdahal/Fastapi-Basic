"""SQLAlchemy setup: engine, sessionmaker, Base class."""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import os

from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()