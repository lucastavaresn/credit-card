import pytest
from credit_card.models.credit_card_schema import CreditCardSchema

@pytest.mark.parametrize("exp_date, expected_result", [
    ("12/2025", True),
    ("01/2022", False),
])
def test_date_format(exp_date, expected_result):
    try:
        result = CreditCardSchema.date_format(exp_date)
        assert expected_result is True
    except ValueError:
        assert expected_result is False

@pytest.mark.parametrize("card_number, expected_result", [
    ("4111111111111111", True),
    ("1234567890123456", False),
])
def test_number_validator(card_number, expected_result):
    try:
        result = CreditCardSchema.number_validator(card_number)
        assert expected_result is True
    except ValueError:
        assert expected_result is False

@pytest.mark.parametrize("cvv, expected_result", [
    ("123", True),
    ("abc", False),
    ("None", False),
])
def test_cvv_validator(cvv, expected_result):
    try:
        result = CreditCardSchema.cvv_validator(cvv)
        assert expected_result is True
    except ValueError:
        assert expected_result is False