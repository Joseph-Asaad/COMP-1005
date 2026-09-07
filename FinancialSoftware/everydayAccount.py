from account import Account


class EverydayAccount(Account):
    def __init__(self, balance, owner, max_withdrawal, name=None):
        super().__init__(balance, owner, name)
        self.__max_withdrawal = max_withdrawal

    def decrease_balance(self, amount):
        if amount > self.__max_withdrawal:
            print(
                f"over ${self.max_withdrawal} withdrawal limit of ", self.get_ID())
            return -1
        super().decrease_balance()

    def set_max_withdrawal(self, new):
        if not isinstance(new, float):
            return
        self.__max_withdrawal = new

    def get_max_withdrawal(self):
        return self.__max_withdrawal

    max_withdrawal = property(
        lambda self: self.__max_withdrawal, set_max_withdrawal)
