from typing import List
from uuid import UUID

from .client import Client


class Bank:
    def __init__(self):
        self.__clients: List[Client] = []

    def __repr__(self) -> str:
        return f"Bank(clients={repr(self.__clients)})"

    def add_client(self, client: Client) -> None:
        if client in self.__clients:
            raise ValueError(f"Client with ID: {client.client_id} already exists")
        self.__clients.append(client)

    def remove_client(self, client: Client) -> None:
        if client not in self.__clients:
            raise ValueError(f"Client with ID: {client.client_id} not found")
        self.__clients.remove(client)

    def get_client(self, client_id: UUID) -> Client:
        for client in self.__clients:
            if client_id == client.client_id:
                return client
        raise ValueError(f"Client with ID: {client_id} not found")

    def print_all_balances(self) -> None:
        print("All client balances:")
        for client in self.__clients:
            print(f"{client.get_balance:.2f}")
