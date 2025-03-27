import re
import pytest

from src.main.bank import Bank
from src.main.client import Client

def test_add_client():
    bank = Bank()
    client_1 = Client("John", 1000)
    client_2 = Client("Alice", 5000)
    client_1_id = bank.add_client(client_1)
    client_2_id = bank.add_client(client_2)
    assert client_1_id != client_2_id
    assert client_1_id == 1
    assert client_2_id == 2
    assert bank.get_client(client_1_id) == client_1
    assert bank.get_client(client_2_id) == client_2

def test_add_existing_client():
    bank = Bank()
    client = Client("John", 1000)
    bank.add_client(client)
    with pytest.raises(ValueError, match=re.escape("Client: Client(name=John, balance=1000) already exists")):
        bank.add_client(client)

def test_remove_client():
    bank = Bank()
    client = Client("John", 1000)
    client_id = bank.add_client(client)
    bank.remove_client(client_id)
    with pytest.raises(ValueError, match=re.escape(f"Client with ID: {client_id} not found")):
        bank.get_client(client_id)

def test_remove_non_existing_client():
    bank = Bank()
    with pytest.raises(ValueError, match=re.escape("Client with ID: 1 not found")):
        bank.remove_client(1)

def test_get_client():
    bank = Bank()
    client = Client("John", 1000)
    client_id = bank.add_client(client)
    assert bank.get_client(client_id) == client

def test_get_non_existing_client():
    bank = Bank()
    with pytest.raises(ValueError, match=re.escape("Client with ID: 1 not found")):
        bank.get_client(1)

def test_print_all_balances(capsys):
    bank = Bank()
    client_1 = Client("John", 1000)
    client_2 = Client("Alice", 5000)
    bank.add_client(client_1)
    bank.add_client(client_2)
    bank.print_all_balances()
    captured = capsys.readouterr()
    assert "All client balances:\n1000\n5000\n" in captured.out
