from abs_repr import AbsRepr
from hasUUID import hasUUID
#from client import Client

class Account(hasUUID, AbsRepr):
    from enum import Enum

    class AccountTypes(Enum):
        SAVINGS = "savings"
        CHECKING = "checking"
        CREDIT = "credit"

    def __init__(self, type, balance, history, owner, interest_rate, name=None):
        super().__init__(self)
        self.__name = name
        self.__type = type
        self.__balance = balance
        self.__history = history,
        self.__owner = owner
        self.__interest_rate = interest_rate

        if name == None:
            self.name = owner.printName(owner.__class__.NameFormats.CASUAL) + "\'s Account"

        owner.add_account(self)

    def increase_balance(self, amount):
        if amount < 0 : 
            return
        self.__balance = self.__balance + amount
        return 1
    def decrease_balance(self, amount):
        if self.__balance < amount:
            print("insufficient funds in account ", self.get_ID)
            return -1
        self.__balance = self.__balance - amount
        return 1
    def get_balance (self) :
        return self.__balance 



    def __str__(self):
        return ("ID_number=" + str(self.ID_number) +
                ", name=" + self.name +
                ", type=" + self.type.value +
                ", balance=" + str(self.balance)
                )
