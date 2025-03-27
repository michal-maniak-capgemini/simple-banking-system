from .client import Client

class Bank:
    def __init__(self):
        self.__client_id = 0
        self.__clients = {}

    def add_client(self, client: Client) -> int:
        if client in self.__clients.values():
            raise ValueError(f"Client: {client} already exists")
        self.__client_id += 1
        self.__clients[self.__client_id] = client
        return self.__client_id

    def remove_client(self, client_id: int):
        if client_id not in self.__clients:
            raise ValueError(f"Client with ID: {client_id} not found")
        del self.__clients[client_id]

    def get_client(self, client_id: int) -> Client:
        if client_id not in self.__clients:
            raise ValueError(f"Client with ID: {client_id} not found")
        return self.__clients[client_id]

    def print_all_balances(self):
        print("All client balances:")
        for client in self.__clients.values():
            print(client.get_balance())
