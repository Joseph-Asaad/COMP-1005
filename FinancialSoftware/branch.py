from hasUUID import hasUUID  # So branches get UUIDs.
# For parsing and checking phone numbers. Yes this is an unapproved external library, but parsing global phone numbers is more work than the rest of this assignment combined by a factor of fifty and it's not assessed so you'll have to forgive me.
import phonenumbers as phonenumbers


class Branch(hasUUID):
    """
    Class that represents a Branch
    Attributes
    ---------
    Methods
    -------
    open() : void
        opens the branch

    close() : void
        closes the branch

    get_branch_number() : int
        returns the branch number

    set_branch_number( branch_number : int) : void
        sets the branch number

    get_address () : str
        returns the address

    set_address (address : str) : void
        sets the address

    get_phone_number() : PhoneNumber
        returns the phone number

    set_phone_number(phone_number : PhoneNumber,str,int) : void
        sets the phone number. If passed an unparsed input, parses it.

    get_name() : str
        returns branch name.

    set_name(name : str) : void
        sets the branch name.
    """

    def __init__(self, branch_number, address, phone_number, is_open=False, name=None):
        hasUUID.__init__(self)  # Assign an ID to this object.
        # Default setters.
        self.set_branch_number(branch_number)
        self.set_address(address)
        self.set_phone_number(phone_number)

        # Open if open, close if close.
        if is_open:
            self.open()
        else:
            self.close()
        # Default name is
        self.set_name(self.get_address() if name == None else name)

    # Open or close the branch.
    def open(self):
        self.__is_open = True
        print("branch", self.__branch_number, "is now open")

    def close(self):
        self.__is_open = False
        print("branch", self.__branch_number, "is now closed")

    def is_open(self):
        return self.__is_open

    # Getter, setter for branch number (note: number is user-facing, not internal ID).
    def get_branch_number(self):
        return self.__branch_number

    def set_branch_number(self, new):
        if (not isinstance(new, int)):
            return
        self.__branch_number = new

    # Getter, setter for address.
    def get_address(self):
        return self.__address

    def set_address(self, new):
        if (not isinstance(new, str)):
            return
        self.__address = new

    # Getter, setter for phone number.
    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, new):
        if not isinstance(new, phonenumbers.PhoneNumber):
            if isinstance(new, str):
                self.set_phone_number(phonenumbers.parse("+1 {}".format(new)))
            return
        self.__phone_number = new

    # Getter, setter for name.
    def get_name(self):
        return self.__name

    def set_name(self, new):
        if (not isinstance(new, str)):
            return
        self.__name = new

    # Override built-in functions.
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
