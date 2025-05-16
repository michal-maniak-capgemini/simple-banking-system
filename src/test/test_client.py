import math

import pytest

from src.main.client import Client
from datetime import datetime

def test_balance_below_0():
    with pytest.raises(ValueError, match="Balance/Amount can't be negative"):
        Client("John", -1)

def test_get_balance():
    client = Client("John", 1000.54)
    assert math.isclose(client.get_balance, 1000.54, rel_tol=1e-09, abs_tol=1e-09)

def test_deposit_negative_amount():
    client = Client("John", 1000)
    with pytest.raises(ValueError, match="Balance/Amount can't be negative"):
        client.deposit(-1)

def test_deposit():
    client = Client("John", 1000)
    client.deposit(500)
    assert client.get_balance == 1500
    client.deposit(1000)
    assert client.get_balance == 2500

def test_withdraw_negative_amount():
    client = Client("John", 1000)
    with pytest.raises(ValueError, match="Balance/Amount can't be negative"):
        client.withdraw(-1)

def test_withdraw_more_than_balance():
    client = Client("John", 1000)
    with pytest.raises(ValueError, match="Can't withdraw more than balance"):
        client.withdraw(1001.50)

def test_withdraw():
    client = Client("John", 1000)
    client.withdraw(500)
    assert client.get_balance == 500

def test_print_statement(mocker, capsys):
    fixed_date = datetime(2021, 7, 1)
    mock_datetime = mocker.patch('src.main.client.datetime')
    mock_datetime.now.return_value = fixed_date

    client = Client("John", 1000)
    client.deposit(500)
    client.withdraw(200)
    client.print_statement()
    captured = capsys.readouterr()

    expected_output = (
    "Client transaction history:\n"
    "Transaction: TransactionType.DEPOSIT of 500 on 2021-07-01 00:00:00 for John\n"
    "Transaction: TransactionType.WITHDRAWAL of 200 on 2021-07-01 00:00:00 for John\n"
    )
    assert captured.out == expected_output

def test_print_statement_when_empty_transactions(mocker, capsys):
    fixed_date = datetime(2021, 7, 1)
    mock_datetime = mocker.patch('src.main.client.datetime')
    mock_datetime.now.return_value = fixed_date

    client = Client("John", 1000)
    client.print_statement()
    captured = capsys.readouterr()

    expected_output = (
        "Client transaction history:\n"
        "2021-07-01 00:00:00 No transactions so far.\n"
    )
    assert captured.out == expected_output
