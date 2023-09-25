from typing import Any, List

from creditcard import CreditCard as CC
from sqlalchemy.orm import Session

from credit_card.models.credit_card import CreditCard
from credit_card.models.credit_card_schema import CreditCardSchema
from credit_card.utils.utils import fernet


class CreditCardRepository:
    def __init__(self, session: Session):
        self.session = session
        self.model = CreditCard

    async def get_all(self) -> List[tuple[Any]]:
        all_cards = self.session.query(self.model).all()
        for card in all_cards:
            card.number = fernet.decrypt(card.number)
        return all_cards

    async def get_by_id(self, card_id: str) -> tuple[Any]:
        all_cards = self.session.query(self.model).filter_by(id=card_id)
        for card in all_cards:
            card.number = fernet.decrypt(card.number)
        return all_cards

    async def save(self, card: CreditCardSchema):
        brand = CC(card.number).get_brand()
        encrypted_number = fernet.encrypt(card.number.encode())
        credit_card = CreditCard(
            exp_date=card.exp_date,
            holder=card.holder,
            number=encrypted_number,
            cvv=card.cvv,
            brand=brand,
        )
        self.session.add(credit_card)
        self.session.commit()
        self.session.refresh(credit_card)

        return credit_card
