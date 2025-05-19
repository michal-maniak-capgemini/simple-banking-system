from uuid import UUID

from src.main.bank import Bank
from src.main.client import Client


class TransactionService:
    def __init__(self, bank: Bank):
        self.__bank: Bank = bank

    def deposit_money_for_a_client(self, client_id: UUID, amount: float) -> None:
        client: Client = self.__bank.get_client(client_id)
        client.deposit(amount)

    def withdraw_money_for_a_client(self, client_id: UUID, amount: float) -> None:
        client: Client = self.__bank.get_client(client_id)
        client.withdraw(amount)
