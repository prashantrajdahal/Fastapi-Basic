"""
Central configuration using pydantic-settings.
Reads from .env file automatically.
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    
    #Database settings
    DATABASE_URL: str
    
    #App metadata
    PROJECT_NAME: str = "FastAPI CRUD"
    VERSION: str= "1.0.0"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True
        
settings = Settings()
    