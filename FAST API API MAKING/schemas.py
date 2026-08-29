# schemas.py
# ------------------------------------------------------
# Ei file e Pydantic Schema define kora hoy.
# Schema = Client theke ja data ashbe (request) ba client ke
# ja data jabe (response) tar "shape/validation rule".
#
# Model (models.py) != Schema (schemas.py)
#   Model  -> Database table structure
#   Schema -> API input/output structure
# ------------------------------------------------------

from pydantic import BaseModel
from typing import Optional


# Client POST/PUT korar somoy ei shape e data pathabe
class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float


# Create korar jonno (POST) — ItemBase theke shobkichu inherit
class ItemCreate(ItemBase):
    pass


# Update korar jonno (PATCH) — shob field optional
class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None


# Response e ja client ke ferot deya hobe (id soho)
class ItemResponse(ItemBase):
    id: int

    class Config:
        from_attributes = True  # SQLAlchemy object -> Pydantic object convert korte dey
