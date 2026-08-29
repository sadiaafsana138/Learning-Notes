# models.py
# ------------------------------------------------------
# Ei file e Database Table define kora hoy (SQLAlchemy Model).
# Ekta class = Ekta table.
# Notun table lagle: ei style e ekta notun class banabe,
# tarpor niche __main__ e "Base.metadata.create_all" call
# hobe (main.py te) jate table ta actual DB te create hoy.
# ------------------------------------------------------

from sqlalchemy import Column, Integer, String, Float
from database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
