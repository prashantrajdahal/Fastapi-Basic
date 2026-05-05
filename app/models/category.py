"""SQLAlchemy model for the 'categories' table."""
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from app.core.database import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=100), unique=True, nullable=False, index=True)
    description = Column(String(length=300), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationship – one category can have many items
    items = relationship("Item", back_populates="category", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Category {self.name}>"