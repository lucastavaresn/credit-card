import os
from credit_card.db.config import Base, engine
from credit_card.utils.auth import AuthMiddleware
from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
from credit_card.routes import credit_card

def init_app() -> FastAPI:

    app = FastAPI()
    app.add_middleware(BaseHTTPMiddleware, dispatch=AuthMiddleware())
    app.include_router(credit_card.router, prefix="/api")
    Base.metadata.create_all(bind=engine)
    return app

