import uuid
from typing import List

from .transaction import Transaction
from .transaction_type import TransactionType
from datetime import datetime


class Client:
    def __init__(self, name: str, balance: float = 0):
        self.__check_if_negative(balance)
        self.client_id: uuid.UUID = uuid.uuid4()
        self.name: str = name
        self.__balance: float = balance
        self.__transactions: List[Transaction] = []

    def __repr__(self) -> str:
        return f"Client(client_id={self.client_id}, name={self.name}, balance={self.__balance}, transactions={self.__transactions})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Client):
            return False
        return self.client_id == other.client_id

    def deposit(self, amount: float) -> None:
        self.__check_if_negative(amount)
        self.__balance += amount
        transaction: Transaction = Transaction(
            self.client_id, TransactionType.DEPOSIT, amount, datetime.now()
        )
        self.__transactions.append(transaction)

    def withdraw(self, amount: float) -> None:
        self.__check_if_negative(amount)
        self.__check_if_more_than_balance(amount)
        self.__balance -= amount
        transaction: Transaction = Transaction(
            self.client_id, TransactionType.WITHDRAWAL, amount, datetime.now()
        )
        self.__transactions.append(transaction)

    @property
    def get_balance(self) -> float:
        return self.__balance

    def print_statement(self) -> None:
        print("Client transaction history:")
        if not self.__transactions:
            print(f"{datetime.now()} No transactions so far.")
        for transaction in self.__transactions:
            print(transaction)

    @staticmethod
    def __check_if_negative(value: float) -> None:
        if value < 0:
            raise ValueError("Balance/Amount can't be negative")

    def __check_if_more_than_balance(self, amount) -> None:
        if amount > self.__balance:
            raise ValueError("Can't withdraw more than balance")
