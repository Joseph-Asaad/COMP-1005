from abs_repr import AbsRepr
from hasUUID import hasUUID

class Transaction(hasUUID, AbsRepr):
    from enum import Enum

    class TransactionTypes(Enum):
        DEPOSIT = "Deposit"
        WITHDRAWAL = "Withdrawal"

    class TransactionStatuses(Enum):
        PENDING = "Pending"
        PROCESSED = "Processed"
        CANCELLED = "Cancelled"

    def __init__(self, type, amount, description):
        self.__type = type
        self.__amount = amount
        self.__description = description
        self.__status = self.TransactionStatuses.PENDING

    def process(self):
        match self.__status:
            case self.TransactionStatuses.PENDING:
                self.__status = self.TransactionStatuses.PROCESSED
                print("Transaction successfully processed")
            case self.TransactionStatuses.PROCESSED:
                print("Error: Transaction is already processed.")
            case self.TransactionStatuses.CANCELLED:
                print("Error: Transaction has been cancelled.")

    def cancel(self):
        match self.__status:
            case self.TransactionStatuses.PENDING:
                self.__status = self.TransactionStatuses.CANCELLED
                print("Transaction successfully cancelled")
            case self.TransactionStatuses.PROCESSED:
                print("Error: Transaction is already processed.")
            case self.TransactionStatuses.CANCELLED:
                print("Error: Transaction has already been cancelled.")

    def __str__(self):
        return ("ID_number=" + str(self.ID_number) +
                ", type=" + self.__type.value +
                ", amount=" + str(self.__amount) +
                ", description=\"" + self.__description + "\"" +
                ", status=" + self.__status.value
                )

    def get_type (self) : 
        return self.__type
    def set_type (self, new) : 
        if not isinstance(type, self.TransactionTypes) : return
        self.__type = new

