from account import Account


class SavingsAccount(Account):
    """

    interest_rate: ....
    """

    def __init__(self, balance, owner, interest_rate, min_balance, name=None):
        super().__init__(balance, owner, name)
        if interest_rate < 0:
            raise ValueError("Must be at least zero")
        self.__interest_rate = interest_rate
        self.__min_balance = min_balance

        # Accounts get a name no matter what, either "New Account" or (eg) "John's Account " if no name is provided.
        if name == None:
            if not owner == None:
                self.set_name(owner.print_name(
                    owner.__class__.NameFormats.CASUAL) + "\'s Savings Account")
            else:
                self.set_name("New Account")

    def set_min_balance(self, min_balance):
        self.__min_balance == min_balance

    def get_min_balance(self):
        return self.__min_balance

        # Getter, setter for interest rate.
    def get_interest_rate(self):
        return self.__interest_rate

    def set_interest_rate(self, new):
        if not isinstance(new, float) and not isinstance(new, int):
            raise TypeError
        if new < 0 or new > 100:
            raise ValueError("Must be between 0% and 100%")
        self.__interest_rate = new

    def decrease_balance(self, amount):
        if self._balance < amount + self.__min_balance:
            raise self.WithdrawalError(
                f"Error: account {self.get_ID()} only contains ${self._balance}, cannot withdraw ${amount} without going below minimum of ${self.__min_balance}")
        self._balance -= amount
        from transaction import Transaction
        self._add_transaction(Transaction.TransactionTypes.DEPOSIT, amount)
        return 1

    interest_rate = property(get_interest_rate, set_interest_rate)
