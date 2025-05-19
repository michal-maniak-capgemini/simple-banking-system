import math
from uuid import UUID

import pytest

from src.main.bank import Bank
from src.main.client import Client
from src.main.service.transaction_service import TransactionService


@pytest.fixture
def client():
    return Client(name="John Doe", balance=1000.00)


@pytest.fixture
def bank(client):
    bank = Bank()
    bank.add_client(client)
    return bank


@pytest.fixture
def transaction_service(bank):
    return TransactionService(bank)


def test_deposit(client, transaction_service):
    transaction_service.deposit_money_for_a_client(client.client_id, 500.00)
    assert math.isclose(client.get_balance, 1500.00, rel_tol=1e-09, abs_tol=1e-09)


def test_deposit_client_not_found(transaction_service):
    my_id = UUID("12345678-1234-5678-1234-567812345678")
    with pytest.raises(ValueError, match=f"Client with ID: {my_id} not found"):
        transaction_service.deposit_money_for_a_client(my_id, 100.00)


def test_withdraw(client, transaction_service):
    transaction_service.withdraw_money_for_a_client(client.client_id, 200.00)
    assert math.isclose(client.get_balance, 800.00, rel_tol=1e-09, abs_tol=1e-09)


def test_withdraw_client_not_found(transaction_service):
    my_id = UUID("12345678-1234-5678-1234-567812345678")
    with pytest.raises(ValueError, match=f"Client with ID: {my_id} not found"):
        transaction_service.withdraw_money_for_a_client(my_id, 100.00)
