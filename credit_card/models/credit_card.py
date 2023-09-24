from sqlalchemy import Boolean, Column, ForeginKey, Integer, String, Date, Numeric
from credit_card.db.config import Base

class CreditCard(Base):
    __tablename__ = "cards"

    id = Column(String, primary_key=True, index=True)
    exp_date = Column(Date(), nullable=False)
    holder = Column(String(150), nullable=False)
    number = Column(String(255), nullable=False)
    cvv = Column(Numeric(4), nullable=True)
    brand = Column(String(20), nullable=False)
