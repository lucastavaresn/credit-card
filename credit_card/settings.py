from typing import Annotated
from credit_card.db.config import SessionLocal
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from credit_card.routes import credit_card

def init_app() -> FastAPI:

    app = FastAPI()

    app.include_router(credit_card.router, prefix="/api")

    return app

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

