from .transaction import Transaction
from .transaction_type import TransactionType
from datetime import datetime

class Client:
    def __init__(self, name: str, balance: int):
        if balance < 0:
            raise ValueError("Balance can't be negative")
        self.name = name
        self.balance = balance
        self.__transactions = []

    def __repr__(self):
        return f"Client(name={self.name}, balance={self.balance})"

    def deposit(self, amount: int):
        if amount < 0:
            raise ValueError("Can't deposit negative amount")
        self.balance += amount
        transaction = Transaction(self.name, TransactionType.DEPOSIT, amount, datetime.now())
        self.__transactions.append(transaction)

    def withdraw(self, amount: int):
        if amount < 0:
            raise ValueError("Can't withdraw negative amount")
        elif amount > self.balance:
            raise ValueError("Can't withdraw more than balance")
        self.balance -= amount
        transaction = Transaction(self.name, TransactionType.WITHDRAWAL, amount, datetime.now())
        self.__transactions.append(transaction)

    def get_balance(self) -> int:
        return self.balance

    def print_statement(self):
        print("Client transaction history:")
        for transaction in self.__transactions:
            print(transaction)
