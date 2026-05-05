"""FastAPI application entry point."""
from fastapi import FastAPI
from app.core.config import settings
from app.core.database import engine, Base
from app.api.v1.endpoints import items

# Create all tables (in production, use Alembic migrations)
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

# Include routers
app.include_router(items.router, prefix="/api/v1")
# Later we'll add categories here.

@app.get("/")
def root():
    return {"message": "FastAPI CRUD is running"}