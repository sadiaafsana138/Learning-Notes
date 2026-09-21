# FastAPI Cheat Sheet — Beginner to Advanced

> Full markdown transcription of `fastapi_cheatsheet.html` (same content, plain markdown so it reads directly on GitHub — the HTML version has nicer interactive styling if you open it locally in a browser).

## 01. Hello World & running  `basic`

```python
# main.py
from fastapi import FastAPI

app = FastAPI(title="My API", version="1.0")

@app.get("/")
def root():
    return {"hello": "world"}
```

*Run it (dev server with auto-reload):*

```bash
$ fastapi dev main.py        # dev, hot-reload
$ fastapi run main.py         # production
$ uvicorn main:app --reload   # classic way
```

> 💡 **Tip:** Interactive docs are auto-generated — open /docs and /redoc .

---

## 02. Path & query params  `basic`

```python
# path param — typed & validated
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"id": item_id}

# query params — anything not in the path
@app.get("/search")
def search(q: str, limit: int = 10,
           active: bool = True):
    return {"q": q, "limit": limit}
```

> 💡 **Tip:** Rule: in the path → path param. Has a default / not in path → query param. Types are auto-converted & validated.

---

## 03. Request body — Pydantic models  `basic`

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True

@app.post("/items")
def create(item: Item):
    return {"saved": item.name,
            "total": item.price}
```

> 💡 **Tip:** JSON body is parsed, validated, and documented automatically from the model. Access fields with dot notation.

---

## 04. Validation & richer types  `intermediate`

```python
from fastapi import Query, Path
from pydantic import BaseModel, Field, EmailStr
from typing import Annotated

@app.get("/users")
def list_users(
    q: Annotated[str | None,
         Query(max_length=50)] = None,
    page: Annotated[int, Query(ge=1)] = 1,
):
    return {"q": q, "page": page}

class User(BaseModel):
    email: EmailStr
    age: int = Field(gt=0, le=120)
    name: str = Field(min_length=2)
```

Constraint Meaning gt / ge greater than / or equal lt / le less than / or equal min/max_length string length pattern= regex match

> 💡 **Tip:** Annotated is the modern (recommended) way to attach Query / Path metadata.

---

## 05. Response model & status codes  `intermediate`

```python
from fastapi import status

class UserOut(BaseModel):
    id: int
    email: str   # note: no password field

@app.post("/users",
    response_model=UserOut,
    status_code=status.HTTP_201_CREATED)
def create_user(u: User):
    return u   # password stripped by response_model
```

> 💡 **Tip:** response_model filters output — great for hiding fields (passwords, internal IDs) and shaping the API contract.

---

## 06. Headers, cookies, forms, files  `intermediate`

```python
from fastapi import Header, Cookie, Form, File, UploadFile
from typing import Annotated

@app.get("/h")
def h(user_agent: Annotated[str | None,
                       Header()] = None):
    return {"ua": user_agent}

@app.post("/login")
def login(username: Annotated[str, Form()],
          password: Annotated[str, Form()]):
    return {"user": username}

@app.post("/upload")
async def upload(file: UploadFile):
    data = await file.read()
    return {"name": file.filename,
            "size": len(data)}
```

> 💡 **Tip:** Forms/files need python-multipart (included in [standard] ).

---

## 07. Error handling  `intermediate`

```python
from fastapi import HTTPException

@app.get("/items/{id}")
def get(id: int):
    if id not in db:
        raise HTTPException(
            status_code=404,
            detail="Item not found")
    return db[id]

# custom global handler
from fastapi.responses import JSONResponse

@app.exception_handler(ValueError)
def on_value_error(request, exc):
    return JSONResponse(
        status_code=400,
        content={"error": str(exc)})
```

---

## 08. Async & concurrency  `advanced`

```python
# use async def when you AWAIT I/O
@app.get("/data")
async def data():
    result = await fetch_from_db()   # non-blocking
    return result

# run blocking code in a threadpool
from fastapi.concurrency import run_in_threadpool

async def endpoint():
    await run_in_threadpool(heavy_sync_fn, arg)
```

> 💡 **Tip:** Rule of thumb: async def + await for async libs (httpx, async DB drivers). Plain def if your code is blocking — FastAPI runs it in a threadpool for you.

---

## 09. Dependency injection  `advanced`

```python
from fastapi import Depends
from typing import Annotated

def pagination(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

Pager = Annotated[dict, Depends(pagination)]

@app.get("/items")
def items(p: Pager):
    return p

# dependency with cleanup (yield)
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
```

> 💡 **Tip:** DI is FastAPI's superpower: reusable logic for auth, DB sessions, pagination, settings. yield deps run cleanup after the response.

---

## 10. Routers & project structure  `advanced`

```python
# routers/users.py
from fastapi import APIRouter

router = APIRouter(prefix="/users",
                   tags=["users"])

@router.get("/")
def list_users(): return [...]

# main.py
from routers import users
app.include_router(users.router)
```

*Typical layout:*

```python
app/
├── main.py          # app + include_router
├── routers/         # endpoints by feature
├── models.py        # pydantic / db models
├── dependencies.py  # shared deps
└── core/config.py   # settings
```

---

## 11. Middleware & CORS  `advanced`

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://myapp.com"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# custom middleware
@app.middleware("http")
async def timing(request, call_next):
    resp = await call_next(request)
    resp.headers["X-Server"] = "fastapi"
    return resp
```

> 💡 **Tip:** CORS is the #1 gotcha for frontend devs — add this if your browser app calls the API.

---

## 12. Auth — OAuth2 + JWT  `advanced`

```python
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt  # pip install pyjwt

oauth2 = OAuth2PasswordBearer(tokenUrl="token")
SECRET = "change-me"

def current_user(token: str = Depends(oauth2)):
    try:
        payload = jwt.decode(token, SECRET,
                     algorithms=["HS256"])
    except jwt.PyJWTError:
        raise HTTPException(401, "Invalid token")
    return payload["sub"]

@app.get("/me")
def me(user: str = Depends(current_user)):
    return {"user": user}
```

> 💡 **Tip:** Hash passwords with pwdlib / bcrypt — never store plaintext. The /token route issues the JWT on login.

---

## 13. Database — SQLModel  `advanced`

```python
# pip install sqlmodel
from sqlmodel import SQLModel, Field, Session, create_engine, select

class Hero(SQLModel, table=True):
    id: int | None = Field(default=None,
                              primary_key=True)
    name: str

engine = create_engine("sqlite:///db.sqlite")
SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as s:
        yield s

@app.post("/heroes")
def add(hero: Hero,
        s: Session = Depends(get_session)):
    s.add(hero); s.commit(); s.refresh(hero)
    return hero
```

> 💡 **Tip:** SQLModel (same author as FastAPI) unifies Pydantic + SQLAlchemy. Also popular: raw SQLAlchemy 2.0, Tortoise ORM.

---

## 14. Background tasks & lifespan  `advanced`

```python
from fastapi import BackgroundTasks

@app.post("/send")
def send(email: str, bg: BackgroundTasks):
    bg.add_task(send_email, email)
    return {"status": "queued"}

# startup / shutdown via lifespan
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    connect_db()        # startup
    yield
    close_db()          # shutdown

app = FastAPI(lifespan=lifespan)
```

> 💡 **Tip:** For heavy/distributed jobs use Celery or ARQ instead of BackgroundTasks.

---

## 15. Testing  `advanced`

```python
# pip install pytest httpx
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"hello": "world"}

def test_create():
    r = client.post("/items",
        json={"name": "x", "price": 9.9})
    assert r.status_code == 200
```

> 💡 **Tip:** Override dependencies in tests with app.dependency_overrides[dep] = fake to mock DBs/auth.

---

## 16. Deploy & production  `advanced`

```python
# run multiple workers
$ fastapi run main.py --workers 4
$ uvicorn main:app --host 0.0.0.0 --port 80 \
      --workers 4

# Dockerfile
FROM python:3.13-slim
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["fastapi", "run", "main.py", "--port", "80"]
```

Concern Tool ASGI server uvicorn / gunicorn Reverse proxy nginx / Caddy / Traefik Config pydantic-settings + .env Migrations Alembic

> 💡 **Tip:** Prod checklist: turn off reload · set CORS origins · use env-based secrets · run behind a proxy · add logging & /health .

---
