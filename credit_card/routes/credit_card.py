
from credit_card.models.credit_card_schema import CreditCardResponseSchema, CreditCardSchema
from credit_card.db.dependency import get_db
from credit_card.repository.credit_card_repository import CreditCardRepository
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(prefix="/v1/credit-card")

@router.get("/", response_model=list[CreditCardResponseSchema])
async def get_cards(db: Session = Depends(get_db)):
    dbs = CreditCardRepository(session=db)
    result = await dbs.get_all()
    return result

@router.get("/{id}", response_model=list[CreditCardResponseSchema])
async def get_cards(id:str , db: Session = Depends(get_db), ):
    dbs = CreditCardRepository(session=db)
    result = await dbs.get_by_id(id)
    if not result:
        raise HTTPException(
            status_code=404, detail='Card not found'
        )
    return result

@router.post("/", response_model=CreditCardResponseSchema)
async def get_cards(data: CreditCardSchema, db: Session = Depends(get_db)):
    dbs = CreditCardRepository(session=db)
    result = await dbs.save(data)
    return result