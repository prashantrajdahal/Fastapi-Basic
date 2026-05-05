"""Business logic for items – database operations."""

from sqlalchemy.orm import Session
from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate

def get(db: Session, item_id: int) -> Item:
    """Retrive an item by its ID"""
    return db.query(Item).filter(Item.id== item_id).first()

def get_multi(db:Session, skip: int=0, limit:int= 100)->list[Item]:
    """Return a list of items with offset/limit."""
    return db.query(Item).offset(skip).limit(limit).all()

def create(db: Session, obj_in: ItemCreate) -> Item:
    """Create a new item in the database."""
    db_obj= Item(**obj_in.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)  # Refresh to get the generated ID and timestamps
    return db_obj

def update(db:Session, db_obj:Item, obj_in: ItemUpdate) -> Item:
    """Update an existing item with new data."""
    update_data= obj_in.dict(exclude_unset=True)  # Only update provided fields
    for field, value in update_data.items():
        setattr(db_obj, field, value)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


