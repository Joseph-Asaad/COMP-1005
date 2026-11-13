from account import Account


class EverydayAccount(Account):
    def __init__(self, balance, owner, max_withdrawal, name=None):
        super().__init__(balance, owner, name)
        self.__max_withdrawal = max_withdrawal

        # Accounts get a name no matter what, either "New Account" or (eg) "John's Account " if no name is provided.
        if name == None:
            if not owner == None:
                self.set_name(owner.print_name(
                    owner.__class__.NameFormats.CASUAL) + "\'s Everyday Account")
            else:
                self.set_name("New Account")

    def decrease_balance(self, amount):
        if amount > self.__max_withdrawal:
            raise self.WithdrawalError(
                f"${amount} is over the ${self.max_withdrawal} withdrawal limit of account {self.name}.")
        if self._balance-amount < 0:
            raise self.WithdrawalError("Cannot go into overdraft!")
        from transaction import Transaction
        self._add_transaction(Transaction.TransactionTypes.DEPOSIT, amount)
        self._balance -= amount

    def set_max_withdrawal(self, new):
        if not isinstance(new, float):
            return
        self.__max_withdrawal = new

    def get_max_withdrawal(self):
        return self.__max_withdrawal

    max_withdrawal = property(
        lambda self: self.__max_withdrawal, set_max_withdrawal)
