"""FastAPI application entry point."""
from fastapi import FastAPI
from sqlalchemy.exc import OperationalError
import time

from app.core.config import settings
from app.core.database import engine, Base
from app.api.v1.endpoints import items, categories

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

# Include routers
app.include_router(items.router, prefix="/api/v1")
app.include_router(categories.router, prefix="/api/v1")


@app.on_event("startup")
def startup_event():
    """Connect to database and create tables on startup with retry logic."""
    retries = 10
    while retries > 0:
        try:
            # Test the connection
            with engine.connect() as conn:
                print("✅ Successfully connected to PostgreSQL!")
                # Create tables if they don't exist
                Base.metadata.create_all(bind=engine)
                print("✅ Database tables created/verified!")
                return
        except OperationalError as e:
            retries -= 1
            wait_time = 5
            print(f"⏳ Waiting for PostgreSQL... ({retries} retries left) Retrying in {wait_time}s")
            time.sleep(wait_time)
    
    raise Exception("❌ Could not connect to PostgreSQL after 10 retries. Exiting.")


@app.get("/")
def root():
    return {"message": "FastAPI CRUD is running"}