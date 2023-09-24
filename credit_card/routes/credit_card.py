
from credit_card.db.credit_card_schema import CreditCardResponseSchema, CreditCardSchema
from credit_card.db.dependency import get_db
from credit_card.repository.credit_card_repository import CreditCardRepository
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/v1/credit-card")

@router.get("/", response_model=list[CreditCardResponseSchema])
async def get_cards(db: Session = Depends(get_db)):
    result = CreditCardRepository(session=db).get_all()
    if not result:
        return {"message": "Not found"}
    return result

@router.get("/{id}")
async def get_card(id:int):
    return {"name": "lucas"}

@router.post("/", response_model=CreditCardResponseSchema)
async def get_cards(data: CreditCardSchema, db: Session = Depends(get_db)):
    print("Proximooooo=====: ", data)
    dbs = CreditCardRepository(session=db)
    result = await dbs.save(data)
    if not result:
        return {"message": "Not found"}
    return result