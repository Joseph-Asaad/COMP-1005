from hasUUID import hasUUID
import phonenumbers as phonenumbers


class Branch(hasUUID):
    def __init__(self, branch_number, address, phone_number, is_open=False, name=None):
        hasUUID.__init__(self)
        self.set_branch_number(branch_number)
        self.set_address(address)
        self.set_phone_number(phone_number)
        if is_open:
            self.open()
        else:
            self.close()
        self.set_name(self.get_address() if name == None else name)

    def open(self):
        self.__is_open = True
        print("branch", self.__branch_number, "is now open")

    def close(self):
        self.__is_open = False
        print("branch", self.__branch_number, "is now closed")

    def get_branch_number(self):
        return self.__branch_number

    def set_branch_number(self, new):
        if (not isinstance(new, int)):
            return
        self.__branch_number = new

    def get_address(self):
        return self.__address

    def set_address(self, new):
        if (not isinstance(new, str)):
            return
        self.__address = new

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, new):
        if not isinstance(new, phonenumbers.PhoneNumber):
            if isinstance(new, str):
                self.set_phone_number(phonenumbers.parse("+1 {}".format(new)))
            return
        self.__phone_number = new

    def get_name(self):
        return self.__name

    def set_name(self, new):
        if (not isinstance(new, str)):
            return
        self.__name = new

    def __str__(self):
        return ("ID_number=" + str(self.get_ID()) +
                ", name=\"" + self.__name + "\"" +
                ", address=\"" + self.__address + "\"" +
                ", phone_number=" + str(self.get_phone_number()) +
                ", is_open=" + str(self.__is_open)
                )

    def __repr__(self):
        return ("ID_number=" + str(self.get_ID()) +
                ", name=\"" + self.__name + "\"" +
                ", address=\"" + self.__address + "\"" +
                ", phone_number=" + str(self.get_phone_number()) +
                ", is_open=" + str(self.__is_open)
                )
