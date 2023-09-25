from credit_card.utils.utils import generate_uuid
import pytest
from unittest import mock


@mock.patch("credit_card.utils.utils.uuid.uuid4")
def test_generate_uuid(mock_get_uuid):
    mock_get_uuid.return_value="4b389e42-ea2c-4d57-92f5-2bfe17501c51"

    result = generate_uuid()
    assert result == "4b389e42-ea2c-4d57-92f5-2bfe17501c51"