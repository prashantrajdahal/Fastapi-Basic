"""SQLAlchemy model for the 'items' table."""
from sqlalchemy import Column, ForeignKey, Integer, String , Float, DateTime, func
from sqlalchemy.orm import relationship
from app.core.database import Base

class Item(Base):
    __tablename__ ="items"
    
    id =Column(Integer,primary_key=True, index=True)
    name= Column(String(length=100),nullable=False ,index=True)
    description= Column(String(length=255), nullable=True)
    price= Column(Float, nullable=False, default=0.0)
    created_at= Column(DateTime(timezone=True), server_default=func.now())
    
    # Foreign key to Category
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True, index=True)

    # Relationship back to Category
    category = relationship("Category", back_populates="items")
    
    def __repr__(self):
        return f"<Item {self.name}>"
