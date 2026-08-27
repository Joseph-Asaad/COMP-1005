from abs_repr import AbsRepr
from hasUUID import hasUUID
from client import Client

class Account(hasUUID, AbsRepr):
    from enum import Enum

    class AccountTypes(Enum):
        SAVINGS = "savings"
        CHECKING = "checking"
        CREDIT = "credit"

    def __init__(self, type, balance, owner, interest_rate, name=None):
        super().__init__(self)
        self.set_name(name)
        self.set_type(type)
        self.__balance = balance
        self.set_owner(owner)
        self.__interest_rate = interest_rate

        if name == None and not owner == None:
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
    
    def get_name (self) : 
        return self.__name
    def set_name (self, new) : 
        if not isinstance(new, str) : return
        self.__name  = new

    def get_owner (self) : 
        return self.__owner
    def set_owner (self, new) : 
        if not isinstance(new, Client) : return
        self.__owner = new

    def get_type (self) : 
        return self.__type
    def set_type (self, new) : 
        if not isinstance(new, self.AccountTypes) : return
        self.__type = new

    def get_interest_rate (self) : 
        return self.__interest_rate
    def set_interest_rate (self, new) : 
        if not isinstance(new, float) or new < 0 or new > 100 : return
        self.__interest_rate = new


    def __str__(self):
        return ("ID_number=" + str(self.get_ID()) +
                ", name=" + self.name +
                ", type=" + self.__type.value +
                ", balance=" + str(self.__balance)
                )
