# ⚡ FastAPI Cheat Sheet — Beginner to Advanced

A single-page, copy-paste-ready reference covering FastAPI from your first endpoint to production-grade async APIs. One sheet is enough.

Built for **FastAPI 0.12x · Pydantic 2 · Python 3.10+** (the current stable line as of 2026).

## What's inside

`fastapi_cheatsheet.html` — 16 sections, organized beginner → advanced, each tagged with a difficulty badge:

**Basics**
1. Hello World & running (`fastapi dev`, `uvicorn`)
2. Path & query parameters
3. Request body with Pydantic models

**Intermediate**
4. Validation & richer types (`Annotated`, `Query`, `Field`)
5. Response models & status codes
6. Headers, cookies, forms, file uploads
7. Error handling (`HTTPException`, custom handlers)

**Advanced**
8. Async & concurrency (`async def`, threadpool)
9. Dependency injection (incl. `yield` cleanup)
10. Routers & project structure
11. Middleware & CORS
12. Auth — OAuth2 + JWT
13. Database with SQLModel
14. Background tasks & lifespan events
15. Testing (`TestClient`, dependency overrides)
16. Deploy & production (workers, Docker, checklist)

## How to use

**Open it:** double-click `fastapi_cheatsheet.html` — it opens in any browser, no server or internet needed (fonts load from Google Fonts when online; it still works offline with fallback fonts).

**Navigate:** click any item in the contents grid to jump to that section.

**Print / save as PDF:** `Ctrl/Cmd + P` → Save as PDF. The stylesheet has a print mode that switches to a clean light theme with readable code.

## Quick start (from the sheet)

```bash
pip install "fastapi[standard]"
fastapi dev main.py          # dev server, hot reload
# open http://127.0.0.1:8000/docs  for interactive Swagger UI
```

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"hello": "world"}
```

## Notes

- `fastapi[standard]` bundles uvicorn, the FastAPI CLI, `python-multipart` (forms/files), and more.
- FastAPI dropped Python 3.8/3.9 support in late 2025 — use **3.12 or 3.13** for new projects.
- All examples use **Pydantic 2** and the modern **`Annotated`** style for parameter metadata.

## Reference

Official documentation: https://fastapi.tiangolo.com
