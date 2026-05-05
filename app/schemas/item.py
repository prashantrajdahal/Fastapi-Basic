"""Pydantic schemas for request/response validation."""
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class ItemBase(BaseModel):
    """Shared fields for items."""
    name: str = Field(..., min_length=1, max_length=100, description="Item name")
    description: Optional[str] = Field(None, max_length=300)
    price: float = Field(..., gt=0, description="Price must be > 0")
    # Inside ItemBase add:
    category_id: Optional[int] = Field(None, description="ID of the category")

class ItemCreate(ItemBase):
    """Schema for creating a new item."""
    pass

class ItemUpdate(BaseModel):
    """Only provided fields will be updated (partial update)."""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=300)
    price: Optional[float] = Field(None, gt=0)
class Item(ItemBase):
    """Schema returned to client."""
    id: int
    created_at: datetime
    class Config:
        orm_mode = True  # enables reading from ORM objects