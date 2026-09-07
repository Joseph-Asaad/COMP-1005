from account import Account


class SavingsAccount(Account):
    def __init__(self, balance, owner, interest_rate, min_balance, name=None):
        super().__init__(balance, owner, name)
        self.__interest_rate = interest_rate
        self.__min_balance = min_balance

        # Getter, setter for interest rate.
    def get_interest_rate(self):
        return self.__interest_rate

    def set_interest_rate(self, new):
        if not isinstance(new, float) or new < 0 or new > 100:
            return
        self.__interest_rate = new

    def decrease_balance(self, amount):
        if self._balance < amount + self.__min_balance:
            print("Error: account ", self.get_ID(),
                  " cannot go below ",  self.__min_balance)
            return -1
        self._balance = self._balance - amount
        return 1

    interest_rate = property(get_interest_rate, set_interest_rate)
