from abs_repr import AbsRepr
from hasUUID import hasUUID
from phonenumbers import phonenumber

class Branch(hasUUID, AbsRepr):
    def __init__(self, branch_number, address, phone_number, is_open=False, name=None):
        self.set_branch_number(branch_number)
        self.set_address(address)
        self.set_phone_number(phone_number)
        if is_open : self.open()
        self.set_name(self.get_address() if name == None else name)

    def open(self):
        self.is_open = True
        print("branch", self.branch_number, "is now open")

    def close(self):
        self.is_open = False
        print("branch", self.branch_number, "is now closed")

    def get_branch_number (self) : 
        return self.__branch_number
    def set_branch_number (self, new) : 
        if (not isinstance(new, int)) : return
        self.__branch_number = new

    def get_address (self) : 
        return self.__address
    def set_address (self, new) : 
        if (not isinstance(new, str)) : return
        self.__address = new

    def get_phone_number (self) : 
        return self.__phone_number
    def set_phone_number (self, new) : 
        if (not isinstance(new, phonenumber)) : return
        self.__phone_number = new

    def get_name (self) : 
        return self.__name
    def set_name (self, new) : 
        if (not isinstance(new, str)) : return
        self.__name = new


    def __str__(self):
        return ("ID_number=" + str(self.ID_number) +
                ", name=\"" + self.name + "\"" +
                ", address=\"" + self.address + "\"" +
                ", phone_number=" + str(self.phone_number) +
                ", is_open=" + str(self.is_open)
                )
