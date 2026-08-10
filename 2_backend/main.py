"""
FastAPI application entrypoint.
Wires together the API routers, DB startup/shutdown events, and
global exception handling. Run locally with:
    uvicorn 2_backend.main:app --reload
"""

from fastapi import FastAPI

from 2_backend.api.routes import router as api_router
from 2_backend.db.connection import init_db, close_db

app = FastAPI(title="my-platform API", version="0.1.0")

# Mount all API routes under /api.
app.include_router(api_router, prefix="/api")


@app.on_event("startup")
async def on_startup():
    # Open the DB connection pool once, at process start.
    await init_db()


@app.on_event("shutdown")
async def on_shutdown():
    # Cleanly close DB connections on process exit.
    await close_db()


@app.get("/health")
async def health_check():
    """Simple liveness probe for uptime monitoring / container orchestration."""
    return {"status": "ok"}
