import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from credit_card.main import app 

client = TestClient(app)

bearer_token = "bdf49c3c3882102fc017ffb661108c63a836d065888a4093994398cc55c2ea2f"

def mock_authenticate_token(token):
    if token != bearer_token:
        return False
    return True

def mock_auth_middleware(request):
    return None 


class MockCreditCardRepository:
    def get_all(self):
        return [...]

    def get_by_id(self, card_id):
        return [...]

    def save(self, card_data):
        return card_data

@patch("credit_card.utils.auth.AuthMiddleware", side_effect=mock_auth_middleware)
@patch("credit_card.repository.credit_card_repository.CreditCardRepository", side_effect=MockCreditCardRepository)
def test_get_cards(mock_auth_middleware, mock_repository):
    headers = {"Authorization": f"Bearer {bearer_token}"}
    response = client.get("/api/v1/credit-card/", headers=headers)

    assert response.status_code == 200

@patch("credit_card.utils.auth.AuthMiddleware", side_effect=mock_auth_middleware)
@patch("credit_card.repository.credit_card_repository.CreditCardRepository", side_effect=MockCreditCardRepository)
def test_get_card_by_id(mock_auth_middleware,mock_repository):
    card_id = "1234567890123456" 
    headers = {"Authorization": f"Bearer {bearer_token}"}
    response = client.get(f"/api/v1/credit-card/{card_id}", headers=headers)

    assert response.status_code == 200


@patch("credit_card.utils.auth.AuthMiddleware", side_effect=mock_auth_middleware)
@patch("credit_card.repository.credit_card_repository.CreditCardRepository", side_effect=MockCreditCardRepository)
def test_create_card(mock_auth_middleware,mock_repository):
    card_data = {
        "exp_date": "12/2027",
        "holder": "Alice",
        "number": "4539578763621486",
        "cvv": "789",
        "brand": "visa"
    }
    headers = {"Authorization": f"Bearer {bearer_token}"}
    response = client.post("/api/v1/credit-card/", json=card_data, headers=headers)

    assert response.status_code == 200
