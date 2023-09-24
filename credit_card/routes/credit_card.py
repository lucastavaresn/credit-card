from fastapi import APIRouter, Depends, status

router = APIRouter(prefix="/v1/credit-card")

@router.get("/")
async def get_cards():
    return [{"name": "lucas"},{"name": "pedro"}]

@router.get("/{id}")
async def get_card(id:int):
    return {"name": "lucas"}
