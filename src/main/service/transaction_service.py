from uuid import UUID

from src.main.bank import Bank


class TransactionService:
    def __init__(self, bank: Bank):
        self.__bank = bank

    def deposit_money_for_a_client(self, client_id: UUID, amount: float):
        client = self.__bank.get_client(client_id)
        client.deposit(amount)

    def withdraw_money_for_a_client(self, client_id: UUID, amount: float):
        client = self.__bank.get_client(client_id)
        client.withdraw(amount)
