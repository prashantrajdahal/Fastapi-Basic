"""API routes for categories."""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api import deps
from app.schemas import category as category_schemas
from app.services import category_service

router = APIRouter(prefix="/categories", tags=["categories"])

@router.post("/", response_model=category_schemas.Category, status_code=status.HTTP_201_CREATED)
def create_category(
    *,
    db: Session = Depends(deps.get_db),
    category_in: category_schemas.CategoryCreate,
):
    return category_service.create(db=db, obj_in=category_in)

@router.get("/", response_model=list[category_schemas.Category])
def read_categories(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
):
    return category_service.get_multi(db, skip=skip, limit=limit)

@router.get("/{category_id}", response_model=category_schemas.Category)
def read_category(
    category_id: int,
    db: Session = Depends(deps.get_db),
):
    category = category_service.get(db, category_id=category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.put("/{category_id}", response_model=category_schemas.Category)
def update_category(
    *,
    db: Session = Depends(deps.get_db),
    category_id: int,
    category_in: category_schemas.CategoryUpdate,
):
    category = category_service.get(db, category_id=category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category_service.update(db=db, db_obj=category, obj_in=category_in)

@router.delete("/{category_id}", response_model=category_schemas.Category)
def delete_category(
    *,
    db: Session = Depends(deps.get_db),
    category_id: int,
):
    category = category_service.remove(db, category_id=category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category