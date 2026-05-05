"""Common dependencies (database session, etc.)."""
from typing import Generator
from app.core.database import SessionLocal

def get_db() -> Generator:
    """Create a new database session per request and close it afterwards."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()