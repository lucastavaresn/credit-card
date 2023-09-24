from credit_card.db.config import Base, engine
from fastapi import FastAPI
from credit_card.routes import credit_card

def init_app() -> FastAPI:

    app = FastAPI()

    app.include_router(credit_card.router, prefix="/api")
    Base.metadata.create_all(bind=engine)
    return app

