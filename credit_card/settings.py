from fastapi import FastAPI
from credit_card.routes import credit_card

def init_app() -> FastAPI:

    app = FastAPI()

    app.include_router(credit_card.router, prefix="/api")

    return app


