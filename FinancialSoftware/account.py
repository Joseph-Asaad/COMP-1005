from hasUUID import hasUUID


class Account(hasUUID):
    from enum import Enum

    # Enumerate possible account types, for type checking.
    class AccountTypes(Enum):
        SAVINGS = "savings"
        CHECKING = "checking"
        CREDIT = "credit"

    def __init__(self, type, balance, owner, interest_rate, name=None):
        hasUUID.__init__(self)  # Assign an ID to this object.
        # Default setters.
        self.set_type(type)
        self.__balance = balance
        self.set_owner(owner)
        self.set_interest_rate(interest_rate)

        # Accounts get a name no matter what, either "New Account" or (eg) "John's Account" if no name is provided.
        if name == None:
            if not owner == None:
                self.set_name(owner.printName(
                    owner.__class__.NameFormats.CASUAL) + "\'s Account")
            else:
                self.set_name("New Account")

        owner.add_account(self)

    # Getter, setter for balance — using increase and decrease instead of just a setter.
    def increase_balance(self, amount):
        if amount < 0:
            return
        self.__balance = self.__balance + amount
        return 1

    def decrease_balance(self, amount):
        if self.__balance < amount:
            print("insufficient funds in account ", self.get_ID())
            return -1
        self.__balance = self.__balance - amount
        return 1

    def get_balance(self):
        return self.__balance

    # Getter, setter for account name
    def get_name(self):
        return self.__name

    def set_name(self, new):
        if not isinstance(new, str):
            return
        self.__name = new

    # Getter, setter for owner.
    def get_owner(self):
        return self.__owner

    def set_owner(self, new):
        from client import Client  # Imported here to avoid circular reference.
        if not type(new) == Client:
            return
        self.__owner = new

    # Getter, setter for type.
    def get_type(self):
        return self.__type

    def set_type(self, new):
        if not isinstance(new, self.AccountTypes):
            return
        self.__type = new

    # Getter, setter for interest rate.
    def get_interest_rate(self):
        return self.__interest_rate

    def set_interest_rate(self, new):
        if not isinstance(new, float) or new < 0 or new > 100:
            return
        self.__interest_rate = new

    # Override built-in functions.
    def __str__(self):
        return ("ID_number=" + str(self.get_ID()) +
                ", name=" + self.__name +
                ", type=" + self.__type.value +
                ", balance=" + str(self.__balance)
                )

    def __repr__(self):
        return ("ID_number=" + str(self.get_ID()) +
                ", name=" + self.__name +
                ", owner=" + str(self.get_owner()) +
                ", type=" + self.__type.value +
                ", balance=" + str(self.__balance)
                )
