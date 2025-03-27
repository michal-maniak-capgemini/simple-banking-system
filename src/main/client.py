from .transaction import Transaction
from .transaction_type import TransactionType
from datetime import datetime

class Client:
    def __init__(self, name: str, balance: int):
        if balance < 0:
            raise ValueError("Balance can't be negative")
        self.name = name
        self.balance = balance
        self.transactions = []

    def __repr__(self):
        return f"Client(name={self.name}, balance={self.balance})"

    def deposit(self, cash: int):
        if cash < 0:
            raise ValueError("Can't deposit negative amount")
        self.balance += cash
        transaction = Transaction(self.name, TransactionType.DEPOSIT, cash, datetime.now())
        self.transactions.append(transaction)

    def withdraw(self, cash: int):
        if cash < 0:
            raise ValueError("Can't withdraw negative amount")
        elif cash > self.balance:
            raise ValueError("Can't withdraw more than balance")
        self.balance -= cash
        transaction = Transaction(self.name, TransactionType.WITHDRAWAL, cash, datetime.now())
        self.transactions.append(transaction)

    def get_balance(self) -> int:
        return self.balance

    def print_statement(self):
        print("Client transaction history: ")
        for transaction in self.transactions:
            print(transaction)
