from typing import List
from uuid import UUID

from src.main.bank import Bank
from src.main.client import Client
from src.main.service.client_management_service import ClientManagementService
from src.main.service.transaction_service import TransactionService


def main():
    bank: Bank = Bank()
    client_service: ClientManagementService = ClientManagementService(bank)
    transaction_service: TransactionService = TransactionService(bank)

    client_names: List[str] = ["Anna", "John", "Michael", "Sarah", "David"]
    clients_ids: List[UUID] = []

    # Add clients to the bank
    for name in client_names:
        client: Client = client_service.add_client_to_bank(name)
        clients_ids.append(client.client_id)

    # Deposit money for each client
    deposit_amounts: List[float] = [1000.50, 2000.70, 1500.10, 3000.00, 500.00]
    for index, client_id in enumerate(clients_ids):
        transaction_service.deposit_money_for_a_client(
            client_id, deposit_amounts[index]
        )

    bank.print_all_balances()

    # Withdraw money for each client
    withdraw_amounts: List[float] = [200.00, 500.00, 300.00, 1000.00, 450.00]
    for index, client_id in enumerate(clients_ids):
        transaction_service.withdraw_money_for_a_client(
            client_id, withdraw_amounts[index]
        )

    bank.print_all_balances()

    # Print statements for each client
    for client_id in clients_ids:
        client: Client = bank.get_client(client_id)
        client.print_statement()

    # Remove clients from the bank
    for client_id in clients_ids:
        client_service.remove_client_from_bank(client_id)


if __name__ == "__main__":
    main()
