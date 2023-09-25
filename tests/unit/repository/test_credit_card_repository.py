from unittest.mock import Mock

import pytest
from sqlalchemy.orm import Session

from credit_card.models.credit_card import CreditCard
from credit_card.models.credit_card_schema import CreditCardSchema
from credit_card.repository.credit_card_repository import CreditCardRepository
from credit_card.utils.utils import fernet


@pytest.mark.asyncio
async def test_get_all():
    """
    Test if you can get all registered cards
    """
    session_mock = Mock(spec=Session)

    card_data = [
        CreditCard(
            id=1,
            exp_date="2025-12-31",
            holder="John Doe",
            number=fernet.encrypt("4539578763621486".encode()),
            cvv="123",
            brand="Visa",
        ),
        CreditCard(
            id=2,
            exp_date="2026-12-31",
            holder="Jane Doe",
            number=fernet.encrypt("4539578763621486".encode()),
            cvv="456",
            brand="MasterCard",
        ),
    ]

    session_mock.query.return_value.all.return_value = card_data

    repo = CreditCardRepository(session_mock)

    result = await repo.get_all() 

    assert len(result) == 2
    assert result[0].id == 1
    assert result[1].id == 2
    assert (
        result[0].number.decode() == "4539578763621486"
    )  
    assert result[1].number.decode() == "4539578763621486"


@pytest.mark.asyncio
async def test_get_by_id():
    """
    Test if you can get one registered card by id
    """
    session_mock = Mock(spec=Session)

    card_id_to_find = "1"

    card_data = [
        CreditCard(
            id="1",
            exp_date="2025-12-31",
            holder="John Doe",
            number=fernet.encrypt("4539578763621486".encode()),
            cvv="123",
            brand="Visa",
        ),
        CreditCard(
            id="2",
            exp_date="2026-12-31",
            holder="Jane Doe",
            number=fernet.encrypt("4539578763621486".encode()),
            cvv="456",
            brand="MasterCard",
        ),
    ]

    session_mock.query.return_value.filter_by.return_value = card_data

    repo = CreditCardRepository(session_mock)

    result = await repo.get_by_id(card_id_to_find)  

    assert result[0].id == card_id_to_find
    assert result[0].number.decode() == "4539578763621486"


@pytest.mark.asyncio
async def test_save():
    """
    Test if you can register/create a new card
    """
    session_mock = Mock(spec=Session)

    card_data = CreditCardSchema(
        exp_date="12/2025",
        holder="Alice Smith",
        number="4539578763621486", 
        cvv="789",
    )

    def mock_save(card):
        assert card.number != card_data.number
        card.id = "1"

    session_mock.add.side_effect = mock_save

    repo = CreditCardRepository(session_mock)

    result = await repo.save(card_data)  

    assert result.id == "1"
    assert result.number != card_data.number  
