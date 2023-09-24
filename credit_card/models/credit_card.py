import uuid
from credit_card.utils import generate_uuid
from sqlalchemy import Column, String, Date, Numeric
from credit_card.db.config import Base

class CreditCard(Base):
    __tablename__ = "cards"

    id = Column(String, name="id", primary_key=True, default=generate_uuid())
    exp_date = Column(Date(), nullable=False)
    holder = Column(String(150), nullable=False)
    number = Column(String(255), nullable=False)
    cvv = Column(Numeric(4), nullable=True)
    brand = Column(String(20), nullable=False)

