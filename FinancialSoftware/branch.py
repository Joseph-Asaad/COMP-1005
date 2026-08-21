from abs_repr import AbsRepr
from hasUUID import hasUUID

class Branch(hasUUID, AbsRepr):
    def __init__(self, ID_number, branch_number, address, phone_number, is_open=False, name=None):
        self.ID_number = ID_number
        self.branch_number = branch_number
        self.address = address
        self._phone_number = phone_number
        self.is_open = is_open
        self.name = self.address if name == None else self.name

    def open(self):
        self.is_open = True
        print("branch", self.branch_number, "is now open")

    def close(self):
        self.is_open = False
        print("branch", self.branch_number, "is now closed")

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, new):
        self._phone_number = new
        print("phone number of branch", self.branch_number, "updated to", new)

    def __str__(self):
        return ("ID_number=" + str(self.ID_number) +
                ", name=\"" + self.name + "\"" +
                ", address=\"" + self.address + "\"" +
                ", phone_number=" + str(self.phone_number) +
                ", is_open=" + str(self.is_open)
                )
