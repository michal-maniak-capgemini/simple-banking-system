from uuid import UUID

from .transaction_type import TransactionType
from datetime import datetime


class Transaction:
    def __init__(
        self,
        client_id: UUID,
        transaction_type: TransactionType,
        transaction_amount: float,
        transaction_date: datetime,
    ):
        self.client_id = client_id
        self.transaction_type = transaction_type
        self.transaction_amount = transaction_amount
        self.transaction_date = transaction_date

    def __repr__(self) -> str:
        return f"Transaction(client_id={self.client_id}, transaction_type={self.transaction_type}, transaction_amount={self.transaction_amount}, transaction_date={self.transaction_date})"

    def __str__(self) -> str:
        return f"Transaction: {self.transaction_type} of {self.transaction_amount:.2f} on {self.transaction_date}"
