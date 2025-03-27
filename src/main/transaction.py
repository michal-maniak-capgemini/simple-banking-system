from .transaction_type import TransactionType
from datetime import datetime

class Transaction:
    def __init__ (self, client_name: str, transaction_type: TransactionType, transaction_amount: int, transaction_date: datetime):
        self.client_name = client_name
        self.transaction_type = transaction_type
        self.transaction_amount = transaction_amount
        self.transaction_date = transaction_date

    def __repr__(self) -> str:
        return f"Transaction type: {self.transaction_type}, Amount: {self.transaction_amount}, Date: {self.transaction_date}, Client Name: {self.client_name}"

    def __str__(self) -> str:
        return f"Transaction: {self.transaction_type} of {self.transaction_amount} on {self.transaction_date} for {self.client_name}"
