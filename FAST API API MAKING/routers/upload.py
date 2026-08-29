# routers/upload.py
# ------------------------------------------------------
# Ei file dekhay: CSV / Excel / JSON file client theke
# upload kore kivabe data DB te niye asha jay (bulk import).
#
# Client (Postman / Swagger UI / frontend) file pathabe
# "multipart/form-data" hisebe -> FastAPI ta "UploadFile"
# diye receive kore.
# ------------------------------------------------------

import io
import pandas as pd
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session

import models
from database import get_db

router = APIRouter(
    prefix="/upload",
    tags=["Upload"],
)


# ---------------- CSV UPLOAD ----------------
# URL: POST /upload/csv
# Postman e: Body -> form-data -> key="file", type=File, tarpor .csv file select koro
@router.post("/csv")
async def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    # 1) File extension check (optional but valo practice)
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only .csv files are allowed")

    # 2) File er raw content (bytes) porlam
    contents = await file.read()

    # 3) bytes -> pandas DataFrame (CSV parse)
    df = pd.read_csv(io.BytesIO(contents))

    # CSV column names emon hote hobe: name, description, price
    # (na thakle KeyError ashbe — real project e validate kore nibe)
    inserted = 0
    for _, row in df.iterrows():
        new_item = models.Item(
            name=row["name"],
            description=row.get("description", None),
            price=row["price"],
        )
        db.add(new_item)
        inserted += 1

    db.commit()
    return {"message": f"{inserted} rows imported from CSV successfully"}


# ---------------- EXCEL UPLOAD (.xlsx) ----------------
# URL: POST /upload/excel
# Extra lagbe: pip install openpyxl
@router.post("/excel")
async def upload_excel(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.filename.endswith((".xlsx", ".xls")):
        raise HTTPException(status_code=400, detail="Only Excel files are allowed")

    contents = await file.read()
    df = pd.read_excel(io.BytesIO(contents))

    inserted = 0
    for _, row in df.iterrows():
        new_item = models.Item(
            name=row["name"],
            description=row.get("description", None),
            price=row["price"],
        )
        db.add(new_item)
        inserted += 1

    db.commit()
    return {"message": f"{inserted} rows imported from Excel successfully"}


# ---------------- JSON UPLOAD (file hisebe, .json) ----------------
# URL: POST /upload/json
# Note: normal JSON body hole UploadFile lagbe na, direct Pydantic
# schema diye "List[ItemCreate]" hisebe receive kora jay (easier).
# Ekhane file hisebe upload er example dekhano hoyeche.
@router.post("/json")
async def upload_json(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.filename.endswith(".json"):
        raise HTTPException(status_code=400, detail="Only .json files are allowed")

    contents = await file.read()
    df = pd.read_json(io.BytesIO(contents))

    inserted = 0
    for _, row in df.iterrows():
        new_item = models.Item(
            name=row["name"],
            description=row.get("description", None),
            price=row["price"],
        )
        db.add(new_item)
        inserted += 1

    db.commit()
    return {"message": f"{inserted} rows imported from JSON successfully"}
