from client import Client
from account import Account
from transaction import Transaction
from branch import Branch

import uuid
import datetime


# Make empty arrays for all object types.
clients = []
accounts = []
transactions = []
branches = []

# Create some branches for testing.
branches.append(Branch(1, "Adelaide", "1300 842 715"))
branches.append(Branch(2, "Florence", "1800 559 204", True))
branches.append(Branch(10, "Dorset", "1800 539 726", False))

# Create test clients.
clients.append(Client(["John", "Citizen"],
                      Client.Titles.MR,
                      datetime.date(2026, 5, 4),
                      "0412 558 903",
                      "john.citizen2000@gmail.com",
                      "10 Downing St., London, England",
                      [],
                      branches[0],
                      Client.ContactMethods.EMAIL
                      ))

clients.append(Client(["Leonardo", "da Vinci"],
                      Client.Titles.SIR,
                      datetime.date(1452, 4, 15),
                      "0487 330 194",
                      "Leo.Painterman@hotmail.com",
                      "Amboise, France",
                      [],
                      branches[1],
                      Client.ContactMethods.PHONE
                      ))

clients.append(Client(["Thomas", "Edward", "Lawrence"],
                      Client.Titles.COLONEL,
                      datetime.date(1935, 5, 19),
                      "0459 772 681",
                      "Lawrence.of.Arabia@mod.gov.uk",
                      "Bovington Camp, Dorset, England",
                      [],
                      branches[2],
                      Client.ContactMethods.PHONE
                      ))


# Create accounts.
accounts.append(Account(Account.AccountTypes.CHECKING,
                        15.32,
                        clients[0],
                        0,
                        "Expenses"
                        ))

accounts.append(Account(Account.AccountTypes.CHECKING,
                        9323534.2,
                        clients[1],
                        0.015))

accounts.append(Account(Account.AccountTypes.SAVINGS,
                        2310.63,
                        clients[2],
                        0.02))

# Create transactions.
transactions.append(Transaction(
    Transaction.TransactionTypes.DEPOSIT, 5, "test transaction 1"))
transactions.append(Transaction(
    Transaction.TransactionTypes.WITHDRAWAL, 10, "test transaction 2"))
transactions.append(Transaction(
    Transaction.TransactionTypes.WITHDRAWAL, 15, "test transaction 3"))

transactions[1].process()  # Process transaction 2.
transactions[2].cancel()  # Cancel transaction 3.
# Try to process transaction 3 — should fail because transaction 3 has been cancelled.
transactions[2].process()

# Demonstrate the formatted name printing.
print("Hi", clients[0].printName(Client.NameFormats.CASUAL))
print("Dear", clients[1].printName(Client.NameFormats.DEFAULT))
print("Hello", clients[2].printName(Client.NameFormats.FORMAL))

# Huzzah, he got knighted — demonstrating changing titles.
clients[2].set_title(Client.Titles.SIR)
print("Hello", clients[2].printName(Client.NameFormats.FORMAL))

# Demonstrate adding and subtracting from account balances, including failure caused by overdraft.
print("Account 1:", accounts[1].get_balance())
accounts[1].increase_balance(10)
print("Account 1:", accounts[1].get_balance())

print("Account 2:", accounts[2].get_balance())
accounts[2].increase_balance(10)
print("Account 2:", accounts[2].get_balance())

print("Account 0:", accounts[0].get_balance())
accounts[0].decrease_balance(50)
print("Account 0:", accounts[0].get_balance())

print("Account 1:", accounts[1].get_balance())
accounts[1].decrease_balance(50)
print("Account 1:", accounts[1].get_balance())

# Demonstrate branches opening and closing.
branches[0].open()
branches[1].close()
branches[1].phone_number = "1800 175 294"

# Printing Clients using both str and repr.
print(clients[1])
print(accounts[2])
print(transactions[1])
print(branches[0])
print("repr representations: ")
print(repr(clients[1]))
print(repr(accounts[2]))
print(repr(transactions[1]))
print(repr(branches[0]))
