from typing import List, Any
from credit_card.db.credit_card_schema import CreditCardCreateSchema, CreditCardSchema
from credit_card.models.credit_card import CreditCard
from creditcard import CreditCard as CC
from sqlalchemy.orm import Session


class CreditCardRepository:
    def __init__(self, session:Session):
        self.session = session
        self.model = CreditCard

    async def get_all(self) -> List[tuple[Any]]:
        return self.session.query(self.model).all()
    
    async def get_by_id(self, card_id:int) -> tuple[Any]:
        return self.session.query(self.model).filter_by(id=card_id).one()
    
    async def save(self, card: CreditCardSchema):
        print("Saveee=======: ", card)
        brand = CC(card.number).get_brand()
        credit_card = CreditCard(
            exp_date= card.exp_date,
            holder=card.holder,
            number=card.number,
            cvv=card.cvv,
            brand=brand
        )
        self.session.add(credit_card)
        self.session.commit()
        self.session.refresh(credit_card)

        return credit_card
