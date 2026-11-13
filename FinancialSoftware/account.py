from hasUUID import hasUUID
from abc import ABC, abstractmethod


class Account(hasUUID,  ABC):
    from enum import Enum
    """
    Class that represesnts an account.

    Attributes
    ----------
    balance : float
        Account Balance
    
    Methods
    -------
        increase_balance(amount) : void
            increases balance by specified amount.
        
        decrease_balance(amount) : void
            decreases balance by specified amount. Errors if overdraft is attempted.
        
        get_balanced() : float
            returns account balance.
        
        get_name() : str
            returns account name.
        
        set_name(name : str) : void
            sets account name to supplied name.
        
        get_owner() : Client
            returns account owner.
        
        set_owner(Client) : void 
            sets account owner. Removes self from old owner's account list, adds self to new owner's account list.

        get_type() : AccountTypes
            returns account type.
        
        set_type(type : Account) : void
            sets account type, ignores non-Account objects.

        get_interest_rate() : float
            returns interest rate
        set_interest_rate(interest_rate : float) : void
            sets new interest rate, bounded between 0, 100%.
    """

    def __init__(self, balance, owner, name=None):
        hasUUID.__init__(self)  # Assign an ID to this object.
        # Default setters.
        self.__name = name
        self._balance = balance
        self.set_owner(owner)
        self.__history = []

        owner.add_account(self)

    # Getter, setter for balance — using increase and decrease instead of just a setter.
    def increase_balance(self, amount):
        if amount < 0:
            return
        self._balance += amount
        from transaction import Transaction
        self._add_transaction(Transaction.TransactionTypes.DEPOSIT, amount)
        return 1

    @abstractmethod
    def decrease_balance(self, amount):
        pass

    def get_balance(self):
        return self._balance

    # Getter, setter for account name
    def get_name(self):
        return self.__name

    def set_name(self, new):
        if not isinstance(new, str):
            return
        self.__name = new

    name = property(get_name, set_name)

    # Getter, setter for owner.
    def get_owner(self):
        return self.__owner

    def set_owner(self, new):
        from client import Client  # Imported here to avoid circular reference.
        if not isinstance(new, Client):
            return
        if hasattr(self, '__owner'):
            self.__owner.remove_account(self)
        self.__owner = new
        self.__owner.add_account(self)

    owner = property(get_owner, set_owner)

    def _add_transaction(self, type, amount, description=""):
        from transaction import Transaction

        self.__history.append(Transaction(type, amount, description))

    def get_history(self):
        return "\n".join(str(transaction) for transaction in self.__history)

    # Override built-in functions.

    def __str__(self):
        from client import Client
        return (f"{self.owner.print_name(Client.NameFormats.DEFAULT)}'s Account \"{self.get_name()}\" with balance ${self.get_balance()}")

    def __repr__(self):
        return ("ID_number=" + str(self.get_ID()) +
                ", name=" + self.__name +
                ", owner=" + str(self.get_owner()) +
                ", balance=" + str(self._balance)
                )

    class WithdrawalError(ValueError):
        """Raised when an invalid withdrawal is attempted"""

        def __init__(self, message="This amount cannot be withdrawn from this account at this time."):
            super().__init__(message)
