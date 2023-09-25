import calendar
import logging
from datetime import datetime
from typing import Optional

from creditcard import CreditCard
from pydantic import BaseModel, Field, field_validator


class CreditCardSchema(BaseModel):
    exp_date: str
    holder: str = Field(min_length=2)
    number: str
    cvv: Optional[str] = Field(min_length=3, max_length=4, default=None)
    brand: Optional[str] = Field(default=None)

    @field_validator("exp_date")
    @classmethod
    def date_format(cls, unformatted_date: str) -> datetime:
        month_year = datetime.strptime(unformatted_date, "%m/%Y").date()
        last_day = cls.last_day_month(year=month_year.year, month=month_year.month)

        exp_date = datetime(month_year.year, month_year.month, last_day)
        if exp_date < datetime.now():
            raise ValueError("The date cannot be earlier than the current one!")

        return exp_date

    @classmethod
    def last_day_month(cls, year: int, month: int) -> int:
        _, last_day = calendar.monthrange(year, month)
        logging.info(
            f"[CreditCardSchema][last_day_month] The last day of month is: {last_day}"
        )
        return last_day

    @field_validator("number")
    @classmethod
    def number_validator(cls, card_number: str) -> str:
        card = CreditCard(card_number)
        if not card.is_valid():
            raise ValueError(f"Invalid card number: {card_number}")

        return card_number

    @field_validator("cvv")
    @classmethod
    def cvv_validator(cls, cvv_number: str) -> str:
        if cvv_number and not cvv_number.isnumeric():
            raise ValueError("The CVV must be numeric")

        return int(cvv_number)


class CreditCardCreateSchema(BaseModel):
    exp_date: str
    holder: str = Field(min_length=2)
    number: str
    cvv: Optional[str] = Field(min_length=3, max_length=4, default=None)


class CreditCardResponseSchema(BaseModel):
    id: str
    exp_date: datetime
    holder: str
    number: str
    cvv: int
    brand: str
