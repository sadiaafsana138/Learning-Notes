# routers/items.py
# ------------------------------------------------------
# Ei file ekta "Router" — related API endpoints ek jaygay
# gucche rakha hoy. Notun feature (e.g. "users") add korte
# gele exact ei file ta copy kore "users.py" banabe, tarpor
# Item -> User, item -> user replace korbe.
#
# CRUD er shob operation (Create, Read, Update, Delete)
# ekhane dekhano ache — pattern ta bujhle je kono API banano jabe.
# ------------------------------------------------------

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import models
import schemas
from database import get_db

# APIRouter() — mini FastAPI app er moto, main app e "include" kora hoy
# prefix -> shob endpoint er age "/items" bosbe
# tags -> Swagger docs (/docs) e group kore dekhabe
router = APIRouter(
    prefix="/items",
    tags=["Items"],
)


# ---------------- CREATE (POST) ----------------
# URL: POST /items/
# Body: schemas.ItemCreate onujayi JSON pathate hobe
# Response: schemas.ItemResponse shape e ferot dibe
@router.post("/", response_model=schemas.ItemResponse)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    new_item = models.Item(
        name=item.name,
        description=item.description,
        price=item.price,
    )
    db.add(new_item)      # DB session e add korlam
    db.commit()            # DB te permanent save korlam
    db.refresh(new_item)   # DB theke fresh data (id soho) fetch korlam
    return new_item


# ---------------- READ ALL (GET) ----------------
# URL: GET /items/?skip=0&limit=10
# skip, limit -> query parameter, pagination er jonno
@router.get("/", response_model=List[schemas.ItemResponse])
def get_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items = db.query(models.Item).offset(skip).limit(limit).all()
    return items


# ---------------- READ ONE (GET by id) ----------------
# URL: GET /items/5
# item_id -> path parameter
@router.get("/{item_id}", response_model=schemas.ItemResponse)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


# ---------------- UPDATE (PATCH) ----------------
# URL: PATCH /items/5
# Body te je field pathabe shudhu shei field update hobe
@router.patch("/{item_id}", response_model=schemas.ItemResponse)
def update_item(item_id: int, updated: schemas.ItemUpdate, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    # exclude_unset=True -> client ja pathay nai shegulo baad
    update_data = updated.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(item, key, value)

    db.commit()
    db.refresh(item)
    return item


# ---------------- DELETE ----------------
# URL: DELETE /items/5
@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(item)
    db.commit()
    return {"message": f"Item {item_id} deleted successfully"}
