# FastAPI Starter Template

Ei README ta ekta complete guide — ekhane shob command, shob pattern, shob explanation deya ache. Ei ekta file dekhe je kono beginner je kono notun API (CRUD hok ba file upload hok) nijei banaite parbe.

---

## 1. Folder Structure

```
FAST API API MAKING/
│
├── main.py                 # Entry point — app create + shob router register
├── requirements.txt        # Dependencies list
├── database.py             # DB connection setup (SQLite)
├── models.py                # DB table structure (SQLAlchemy)
├── schemas.py                # API input/output shape (Pydantic)
├── routers/
│   ├── __init__.py
│   ├── items.py              # CRUD example (Create/Read/Update/Delete)
│   └── upload.py              # CSV/Excel/JSON file upload example
└── README.md
```

**Kon file e ki thake — mind e rakho:**

| File | Ki thake | Kobe touch korbe |
|---|---|---|
| `models.py` | DB table (column, type) | Notun table lagle |
| `schemas.py` | Request/Response shape (validation) | Notun data structure lagle |
| `routers/*.py` | Actual endpoint (`@router.get`, `.post` etc.) | Notun API lagle |
| `main.py` | Router include, app config | Notun router file banale |
| `database.py` | DB connection | Shudhu ekbar setup, pore prai touch lagbe na |

---

## 2. Setup Commands (first time only)

```bash
# Project folder e virtual environment banao
python -m venv venv

# Activate koro (Windows)
venv\Scripts\activate

# Activate koro (Mac/Linux)
source venv/bin/activate

# Dependencies install koro
pip install fastapi uvicorn[standard] sqlalchemy pydantic pandas openpyxl python-multipart

# ba requirements.txt thakle:
pip install -r requirements.txt
```

## 3. Run Commands

```bash
# Server run koro (code change korle auto-reload hobe)
uvicorn main:app --reload

# Different port e run korte chaile
uvicorn main:app --reload --port 8080

# Network er onno device theke access korte dile
uvicorn main:app --reload --host 0.0.0.0
```

Server chalu hole:
- App: http://127.0.0.1:8000
- **Swagger docs (test korar sohoj jaiga): http://127.0.0.1:8000/docs**
- Redoc docs: http://127.0.0.1:8000/redoc

> Beginner der jonno: API test korte Postman lagbe na — `/docs` e giye "Try it out" button e click kore direct test kora jay.

## 4. Useful Dev Commands

```bash
# Installed package list dekhte
pip list

# requirements.txt update korte (current env er package likhe rakhbe)
pip freeze > requirements.txt

# Virtual environment theke ber howa
deactivate

# SQLite DB file (app.db) er data dekhte (optional tool)
# DB Browser for SQLite install kore app.db file open korle GUI te data dekha jabe
```

---

## 5. Notun API Kivabe Banabe — Generic Pattern (Step by Step)

Ei 5 step **shob shomoy** same order e follow korbe, subject jaই hok (users, orders, products, students — je kono kichu):

### Step 1 — Model (`models.py`) e table add koro

```python
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
```

### Step 2 — Schema (`schemas.py`) e shape add koro

```python
class UserCreate(BaseModel):
    name: str
    email: str

class UserResponse(UserCreate):
    id: int
    class Config:
        from_attributes = True
```

### Step 3 — Router (`routers/users.py`) banao — `items.py` copy kore edit koro

```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models, schemas
from database import get_db

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/", response_model=List[schemas.UserResponse])
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

@router.get("/{user_id}", response_model=schemas.UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted"}
```

### Step 4 — `main.py` e register koro

```python
from routers import items, users   # notun import
app.include_router(users.router)   # notun line
```

### Step 5 — Test koro

Server restart (ba `--reload` thakle automatic) → `/docs` e giye "Users" section e notun endpoints dekha jabe → "Try it out" diye test koro.

---

## 6. HTTP Methods Cheat Sheet (CRUD)

| Method | Kaj | Example |
|--------|-----|---------|
| GET    | Data read/fetch | `/items/`, `/items/1` |
| POST   | Notun data create | `/items/` |
| PUT    | Full update (shob field required) | `/items/1` |
| PATCH  | Partial update (khali change hobe shudhu shei field) | `/items/1` |
| DELETE | Data delete | `/items/1` |

- **Path parameter**: `/items/{item_id}` → URL er moddhe id
- **Query parameter**: `/items/?skip=0&limit=10` → URL er `?` er por
- **Request body**: JSON data, Pydantic schema diye auto-validate hoy
- **`response_model`**: response e exactly ki field jabe seta control kore
- **`HTTPException`**: error hole proper status code soho message pathay (404 = not found, 400 = bad request, 401 = unauthorized)

---

## 7. File Upload (CSV / Excel / JSON theke Data Neya)

`routers/upload.py` e ei pattern deya ache. Kaj kore emon: client ekta file pathay → server oita porey → DB te save kore.

### CSV upload

```python
import io, pandas as pd
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
import models
from database import get_db

router = APIRouter(prefix="/upload", tags=["Upload"])

@router.post("/csv")
async def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only .csv files are allowed")

    contents = await file.read()                 # file er raw bytes poRlam
    df = pd.read_csv(io.BytesIO(contents))         # bytes -> pandas DataFrame

    for _, row in df.iterrows():                   # row by row DB te insert
        db.add(models.Item(name=row["name"], description=row.get("description"), price=row["price"]))
    db.commit()
    return {"message": f"{len(df)} rows imported"}
```

CSV file er format emon hote hobe (column name gula model er field er sathe match korbe):

```csv
name,description,price
Laptop,Dell i5,55000
Mouse,Wireless mouse,800
```

### Excel (.xlsx) upload

Same pattern, khali `pd.read_excel()` use hobe. Extra lagbe: `pip install openpyxl`

### JSON file upload

Same pattern, `pd.read_json()` use hobe. (Note: normal JSON body hole file upload lagbe na, direct `List[schemas.ItemCreate]` schema diye receive kora jay — beshi common ei way ta.)

### Kivabe test korbe

**Swagger UI (`/docs`) diye:**
1. `/upload/csv` endpoint e click koro
2. "Try it out" → "Choose File" diye `.csv` file select koro
3. "Execute" click koro

**curl diye:**
```bash
curl -X POST "http://127.0.0.1:8000/upload/csv" -F "file=@data.csv"
```

**Postman diye:**
- Method: POST, URL: `http://127.0.0.1:8000/upload/csv`
- Body → form-data → key = `file` (type: File) → file select koro → Send

> Note: Upload feature use korte hole `main.py` e `from routers import items, upload` ar `app.include_router(upload.router)` add korte hobe, ar `requirements.txt` e `pandas`, `openpyxl`, `python-multipart` add korte hobe. (Ekhono add kora hoy nai — chaile bolo, add kore dibo.)

---

## 8. Normal JSON List Upload (file chara, direct body diye — sohoj way)

Multiple item ekbare create korte chaile file upload lagbe na, shudhu ekta list-accepting endpoint likhle hoy:

```python
@router.post("/bulk", response_model=List[schemas.ItemResponse])
def create_items_bulk(items: List[schemas.ItemCreate], db: Session = Depends(get_db)):
    new_items = [models.Item(**item.dict()) for item in items]
    db.add_all(new_items)
    db.commit()
    return new_items
```

Swagger e ekta JSON array body pathabe:
```json
[
  {"name": "Laptop", "description": "Dell i5", "price": 55000},
  {"name": "Mouse", "description": "Wireless", "price": 800}
]
```

---

## 9. Common Errors & Fix

| Error | Karon | Fix |
|---|---|---|
| `404 Not Found` | Wrong URL/id | URL check koro, `/docs` e endpoint list dekho |
| `422 Unprocessable Entity` | Request body schema match kore nai | Schema er required field gula thik ache kina check koro |
| `KeyError` (CSV upload) | CSV column name model er field er sathe mile nai | CSV header ta `name,description,price` emon rakho |
| `ModuleNotFoundError: pandas` | Package install hoy nai | `pip install pandas openpyxl` |
| Server e change dekha jacche na | `--reload` flag deya nai | `uvicorn main:app --reload` diye run koro |
