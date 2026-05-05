"""API routes for items."""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api import deps
from app.schemas import item as item_schemas
from app.services import item_service

router= APIRouter(prefix="/items", tags=["items"])

@router.post("/", response_model=item_schemas.Item, status_code=status.HTTP_201_CREATED)
def create_item(
    *,
    db: Session =Depends(deps.get_db),
    item_in: item_schemas.ItemCreate
):
    """Create a new item."""
    return item_service.create(db=db, obj_in=item_in)

@router.get("/", response_model=list[item_schemas.Item])
def read_items(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
):
    """Retrieve all items with pagination."""
    return item_service.get_multi(db, skip=skip, limit=limit)

@router.get("/{item_id}", response_model=item_schemas.Item)
def read_item(
    item_id: int,
    db: Session = Depends(deps.get_db),
):
    """Retrieve a single item by its ID."""
    item = item_service.get(db, item_id=item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.put("/{item_id}", response_model=item_schemas.Item)
def update_item(
    *,
    db: Session = Depends(deps.get_db),
    item_id: int,
    item_in: item_schemas.ItemUpdate,
):
    """Update an item (partial update)."""
    item = item_service.get(db, item_id=item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item_service.update(db=db, db_obj=item, obj_in=item_in)

@router.delete("/{item_id}", response_model=item_schemas.Item)
def delete_item(
    *,
    db: Session = Depends(deps.get_db),
    item_id: int,
):
    """Delete an item."""
    item = item_service.remove(db, item_id=item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item