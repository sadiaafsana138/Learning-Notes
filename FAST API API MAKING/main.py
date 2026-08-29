# main.py
# ------------------------------------------------------
# Ei file "entry point" — server run korle ei file theke shuru hoy.
# Kaj: FastAPI app create kora, database table create kora,
# ar shob router ke app er sathe "include" kora.
#
# Notun router add korte hole:
#   1. from routers import <notun_file_name>
#   2. app.include_router(<notun_file_name>.router)
# ------------------------------------------------------

from fastapi import FastAPI

import models
from database import engine
from routers import items, upload

# App start howar age DB table create kore nibe (jodi na thake)
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="My FastAPI Project",
    description="Template project — ekhane notun API add kore shikhbo",
    version="1.0.0",
)


# Root endpoint — test korar jonno
# URL: GET /
@app.get("/")
def read_root():
    return {"message": "FastAPI server is running. Go to /docs to test the APIs."}


# items.py te lekha shob endpoint ekhane register hocche
app.include_router(items.router)

# upload.py te lekha CSV/Excel/JSON upload endpoint ekhane register hocche
app.include_router(upload.router)

# ------------------------------------------------------
# Notun API/module add korle example:
#
# from routers import users
# app.include_router(users.router)
# ------------------------------------------------------
