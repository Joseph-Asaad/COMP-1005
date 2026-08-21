from abs_repr import AbsRepr
from hasUUID import hasUUID

class Account(hasUUID, AbsRepr):
    from enum import Enum

    class AccountTypes(Enum):
        SAVINGS = "savings"
        CHECKING = "checking"
        CREDIT = "credit"

    def __init__(self, type, balance, history, owner, interest_rate, name=None):
     
        self.__name = name
        self.__type = type
        self.__balance = balance
        self.__history = history,
        self.__owner = owners
        self.__members = members
        self.__interest_rate = interest_rate

        if name == None:
            self.name = owners[0].names[0] + "\'s Account"

        for client in owners:
            client.accounts.append(self)
        for client in members:
            client.accounts.append(self)

    def increase_balance(self, amount):
        if amount < 0 : 
            return
        self.balance = self.balance + amount
        return 1

    def decrease_balance(self, amount):
        if self.balance < amount:
            print("insufficient funds in account ", self.ID_number)
            return -1
        self.balance = self.balance - amount
        return 1



    def __str__(self):
        return ("ID_number=" + str(self.ID_number) +
                ", name=" + self.name +
                ", type=" + self.type.value +
                ", balance=" + str(self.balance)
                )
