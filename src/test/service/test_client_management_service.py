import pytest

from src.main.bank import Bank
from src.main.service.client_management_service import ClientManagementService


@pytest.fixture
def bank():
    return Bank()


@pytest.fixture
def client_management_service(bank):
    return ClientManagementService(bank)


def test_add_client_to_bank(bank, client_management_service):
    client = client_management_service.add_client_to_bank("John")
    assert client == bank.get_client(client.client_id)


def test_remove_client_from_bank(bank, client_management_service):
    client = client_management_service.add_client_to_bank("John")
    client_management_service.remove_client_from_bank(client.client_id)
    with pytest.raises(
        ValueError, match=f"Client with ID: {client.client_id} not found"
    ):
        bank.get_client(client.client_id)
