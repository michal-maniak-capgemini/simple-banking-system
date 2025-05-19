from uuid import UUID

from src.main.bank import Bank
from src.main.client import Client


class ClientManagementService:
    def __init__(self, bank: Bank):
        self.__bank = bank

    def add_client_to_bank(self, client_name: str) -> Client:
        client = Client(name=client_name)
        self.__bank.add_client(client)
        return client

    def remove_client_from_bank(self, client_id: UUID) -> None:
        client = self.__bank.get_client(client_id)
        self.__bank.remove_client(client)
