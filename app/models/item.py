"""SQLAlchemy model for the 'items' table."""
from sqlalchemy import Column, Integer, String , Float, DateTime, func
from app.core.database import Base

class Item(Base):
    __tablename__ ="items"
    
    id =Column(Integer,primary_key=True, index=True)
    name= Column(String(length=100),nullable=False ,index=True)
    description= Column(String(length=255), nullable=True)
    price= Column(Float, nullable=False, default=0.0)
    created_at= Column(DateTime(timezone=True), server_default=func.now())
    
    def __repr__(self):
        return f"<Item {self.name}>"
