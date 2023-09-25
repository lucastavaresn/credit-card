from credit_card.models.credit_card_schema import CreditCardSchema
import pytest
from unittest.mock import Mock
from credit_card.repository.credit_card_repository import CreditCardRepository
from credit_card.models.credit_card import CreditCard
from credit_card.utils.utils import fernet
from sqlalchemy.orm import Session

# Use pytest.mark.asyncio para testar coroutines assíncronas
@pytest.mark.asyncio
async def test_get_all():
    # Crie um mock da classe Session
    session_mock = Mock(spec=Session)

    # Mock de dados para simular o retorno do banco de dados
    card_data = [
        CreditCard(id=1, exp_date="2025-12-31", holder="John Doe", number=fernet.encrypt("4539578763621486".encode()), cvv="123", brand="Visa"),
        CreditCard(id=2, exp_date="2026-12-31", holder="Jane Doe", number=fernet.encrypt("4539578763621486".encode()), cvv="456", brand="MasterCard"),
    ]

    # Configurar o mock da sessão para retornar os dados de mock quando query é chamado
    session_mock.query.return_value.all.return_value = card_data

    # Crie uma instância da classe CreditCardRepository com o mock da sessão
    repo = CreditCardRepository(session_mock)

    # Chame o método get_all da classe de repositório
    result = await repo.get_all()  # Aguarde a coroutine

    # Verifique se o método retorna os dados de mock após a descriptografia
    assert len(result) == 2
    assert result[0].id == 1
    assert result[1].id == 2
    assert result[0].number.decode() == "4539578763621486"  # Note que o número foi descriptografado
    assert result[1].number.decode() == "4539578763621486"

@pytest.mark.asyncio
async def test_get_by_id():
    # Crie um mock da classe Session
    session_mock = Mock(spec=Session)

    # ID do cartão que desejamos buscar
    card_id_to_find = "1"

    # Mock de dados para simular o retorno do banco de dados
    card_data = [
        CreditCard(id="1", exp_date="2025-12-31", holder="John Doe", number=fernet.encrypt("4539578763621486".encode()), cvv="123", brand="Visa"),
        CreditCard(id="2", exp_date="2026-12-31", holder="Jane Doe", number=fernet.encrypt("4539578763621486".encode()), cvv="456", brand="MasterCard"),
    ]

    # Configure o mock da sessão para retornar os dados de mock quando query é chamado
    session_mock.query.return_value.filter_by.return_value = card_data

    # Crie uma instância da classe CreditCardRepository com o mock da sessão
    repo = CreditCardRepository(session_mock)

    # Chame o método get_by_id da classe de repositório
    result = await repo.get_by_id(card_id_to_find)  # Aguarde a coroutine

    # Verifique se o método retorna o cartão com o ID correto após a descriptografia
    assert result[0].id == card_id_to_find
    assert result[0].number.decode() == "4539578763621486"

@pytest.mark.asyncio
async def test_save():
    # Crie um mock da classe Session
    session_mock = Mock(spec=Session)

    # Dados de teste para um cartão a ser salvo
    card_data = CreditCardSchema(
        exp_date="12/2025",
        holder="Alice Smith",
        number="4539578763621486",  # Número não criptografado
        cvv="789",
    )

    # Configure o mock da sessão para simular o comportamento do método save
    def mock_save(card):
        # Verifique se os dados foram criptografados corretamente
        assert card.number != card_data.number
        # Simule a adição do cartão à sessão e a atualização do ID
        card.id = "1"

    session_mock.add.side_effect = mock_save

    # Crie uma instância da classe CreditCardRepository com o mock da sessão
    repo = CreditCardRepository(session_mock)

    # Chame o método save da classe de repositório
    result = await repo.save(card_data)  # Aguarde a coroutine

    # Verifique se o método retorna o cartão com o ID correto após a descriptografia
    assert result.id == "1"
    assert result.number != card_data.number  # Verifique se o número foi criptografado