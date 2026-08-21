from client import Client
from account import Account
from transaction import Transaction
from branch import Branch

import uuid
import datetime

clients = []
accounts = []
transactions = []
branches = []

branches.append(Branch(uuid.uuid4(), 1, "Adelaide", "1300 842 715"))
branches.append(Branch(uuid.uuid4(), 2, "Florence", "1800 559 204", True))
branches.append(Branch(uuid.uuid4(), 3, "Dorset", "1800 539 726", False))

clients.append(Client(uuid.uuid4(),
                      ["John", "Citizen"],
                      Client.Titles.MR,
                      datetime.date(2026, 5, 4),
                      "0412 558 903",
                      "john.citizen2000@gmail.com",
                      "10 Downing St., London, England",
                      [],
                      branches[0]
                      ))

clients.append(Client(uuid.uuid4(),
                      ["Leonardo", "da Vinci"],
                      Client.Titles.SIR,
                      datetime.date(1452, 4, 15),
                      "0487 330 194",
                      "Leo.Painterman@hotmail.com",
                      "Amboise, France",
                      branches[1],
                      []
                      ))

clients.append(Client(uuid.uuid4(),
                      ["Thomas", "Edward", "Lawrence"],
                      Client.Titles.COLONEL,
                      datetime.date(1935, 5, 19),
                      "0459 772 681",
                      "Lawrence.of.Arabia@mod.gov.uk",
                      "Bovington Camp, Dorset, England",
                      branches[2],
                      []
                      ))

accounts.append(Account(uuid.uuid4(),
                        Account.AccountTypes.CHECKING,
                        15.32,
                        [],
                        [next(filter(lambda x: x.printName(Client.NameFormats.CASUAL)  == "Citizen", clients), None)],
                        [],
                        0))

accounts.append(Account(uuid.uuid4(),
                        Account.AccountTypes.CHECKING,
                        9323534.2,
                        [],
                        [next(filter(lambda x: x.names[-1] ==
                              "da Vinci", clients), None)],
                        [],
                        0.015))

accounts.append(Account(uuid.uuid4(),
                        Account.AccountTypes.SAVINGS,
                        2310.63,
                        [],
                        [next(filter(lambda x: x.names[-1] ==
                              "Lawrence", clients), None)],
                        [next(filter(lambda x: x.names[-1] ==
                              "da Vinci", clients), None)],
                        0.02))

transactions.append(Transaction(
    uuid.uuid4(), Transaction.TransactionTypes.DEPOSIT, 5, "test transaction 1"))
transactions.append(Transaction(
    uuid.uuid4(), Transaction.TransactionTypes.WITHDRAWAL, 10, "test transaction 2"))
transactions.append(Transaction(
    uuid.uuid4(), Transaction.TransactionTypes.WITHDRAWAL, 15, "test transaction 3"))

transactions[1].process()
transactions[2].cancel()
transactions[2].process()



print("Hi", clients[0].printName(Client.NameFormats.CASUAL))
print("Dear", clients[1].printName(Client.NameFormats.DEFAULT))
print("Hello", clients[2].printName(Client.NameFormats.FORMAL))

clients[2].title = Client.Titles.SIR  # yay he got knighted
print("Hello", clients[2].printName(Client.NameFormats.FORMAL))

print("Account 1:", accounts[1].balance)
accounts[1].increase_balance(10)
print("Account 1:", accounts[1].balance)

print("Account 2:", accounts[2].balance)
accounts[2].increase_balance(10)
print("Account 2:", accounts[2].balance)

print("Account 0:", accounts[0].balance)
accounts[0].decrease_balance(50)
print("Account 0:", accounts[0].balance)

print("Account 1:", accounts[1].balance)
accounts[1].decrease_balance(50)
print("Account 1:", accounts[1].balance)

branches[0].open()
branches[1].close()
branches[1].phone_number = "1800 175 294"

print(clients[1])
print(accounts[2])
print(transactions[1])
print(branches[0])
print("repr representations: ")
print(repr(clients[1]))
print(repr(accounts[2]))
print(repr(transactions[1]))
print(repr(branches[0]))
