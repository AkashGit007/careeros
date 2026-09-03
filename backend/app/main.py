from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings

app = FastAPI(
    title="CareerOS API",
    description="AI-powered Career Operating System — backend API.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", tags=["system"])
def health_check() -> dict:
    """Basic liveness check. No auth required."""
    return {"status": "ok", "environment": settings.environment}


# Routers are registered here as they're implemented, e.g.:
# from app.api import auth
# app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
