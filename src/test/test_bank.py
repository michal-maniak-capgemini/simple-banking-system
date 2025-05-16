import re
import uuid

import pytest

from src.main.bank import Bank
from src.main.client import Client

@pytest.fixture()
def client_1():
    return Client("John", 1000.00)

@pytest.fixture()
def client_2():
    return Client("Alice", 5000.00)

@pytest.fixture()
def bank():
    return Bank()

def test_add_client(bank, client_1, client_2):
    bank.add_client(client_1)
    bank.add_client(client_2)
    assert bank.get_client(client_1.client_id) is client_1
    assert bank.get_client(client_1.client_id) is not client_2
    assert bank.get_client(client_2.client_id) is client_2
    assert bank.get_client(client_2.client_id) is not client_1

def test_add_existing_client(bank, client_1):
    bank.add_client(client_1)
    with pytest.raises(ValueError, match=f"Client with ID: {client_1.client_id} already exists"):
        bank.add_client(client_1)

def test_remove_client(bank, client_1):
    bank.add_client(client_1)
    bank.remove_client(client_1)
    with pytest.raises(ValueError, match=f"Client with ID: {client_1.client_id} not found"):
        bank.get_client(client_1.client_id)

def test_remove_non_existing_client(bank, client_1):
    with pytest.raises(ValueError, match=f"Client with ID: {client_1.client_id} not found"):
        bank.remove_client(client_1)

def test_get_client(bank, client_1):
    bank.add_client(client_1)
    assert bank.get_client(client_1.client_id) == client_1

def test_get_non_existing_client(bank):
    my_uuid = uuid.uuid4()
    with pytest.raises(ValueError, match=f"Client with ID: {my_uuid} not found"):
        bank.get_client(my_uuid)

def test_print_all_balances(capsys, bank, client_1, client_2):
    bank.add_client(client_1)
    bank.add_client(client_2)
    bank.print_all_balances()
    captured = capsys.readouterr()
    assert "All client balances:\n1000.00\n5000.00\n" in captured.out
