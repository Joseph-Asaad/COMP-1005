from hasUUID import hasUUID  # So clients get UUIDS.
import datetime  # For Date of Birth.
import phonenumbers as phonenumbers  # For phone numbers.


class Client(hasUUID):
    from enum import Enum
    """
    Methods
    -------
    print_name(format : NameFormats) : str
        returns owner's name in specified format.
    
    set_name(name : str[]) : void
        sets name to provided name.

    set_title(title : Titles(Enum)) : void
        sets title to provided title : Mr, Ms, Mrs, Dr, Sir, Col.

    get_dob() : datetime.date
        returns date of birth.

    set_dob(dob : datetime.date) : void
        sets date of birth.

    get_phone() : PhoneNumber
        returns phone number.

    set_phone (phone : PhoneNumber) : void
        sets phone number.

    get_email() : str
        returns client's email address.

    set_email(email : str) : void
        sets client's email address.
    
    get_address() : str
        returns client's address.
    
    set_address(address : str) : void
        sets client's address.
    
    get_preferred_branch() : Branch
        gets client's preferred branch.
    
    set_preferred_branch(branch : Branch) : void
        sets client's preferred branch.
    
    get_preferred_contact_method() : ContactMethods
        gets client's preferred contact method.
    
    set_preferred_contact_method(contact_method : ContactMethods) : void
        sets client's preferred contact method.
    
    """

    def __init__(self, names, title, dob, phone, email, address, accounts, preferred_branch, preferred_contact_method=None):
        hasUUID.__init__(self)  # Assign an ID to this object.
        # Default setters for attributes.
        self.set_name(names)
        self.set_title(title)
        self.set_dob(dob)
        self.set_phone(phone)
        self.set_email(email)
        self.set_address(address)
        self.set_preferred_branch(preferred_branch)

        self.__accounts = []  # Allow accounts to be added on initialisation.
        for acc in accounts:
            self.add_account(acc)

        # Default contact method is phone.
        self.set_preferred_contact_method(self.ContactMethods.PHONE)
        # In case of the argument being left blank, the set_preferred_contact_method() method will reject a "None" type and do nothing.
        self.set_preferred_contact_method(preferred_contact_method)

    # Enumerates titles. Yes it's hard-coded, but it's easy to edit and a single source-of-truth.
    class Titles(Enum):
        MR = "Mr."
        MS = "Ms."
        MRS = "Mrs."
        DR = "Dr."
        SIR = "Sir"
        COLONEL = "Col."

    class ContactMethods(Enum):  # Ditto for contact methods.
        EMAIL = "email"
        PHONE = "phone"

    # Double Ditto for name formats. This one shouldn't be edited without editing printName() to support new methods.
    class NameFormats(Enum):
        DEFAULT = 0
        FULL = 1
        FORMAL = 2
        CASUAL = 3

    def printName(self, format):  # Prints names.
        match format:
            case self.NameFormats.DEFAULT:  # E.g. John Smith.
                return self.__names[0] + " " + self.__names[-1]
            case self.NameFormats.FULL:  # E.g. John Henry Smith.
                return ' '.join(self.__names)
            case self.NameFormats.FORMAL:  # E.g. Mr. Smith.
                return self.__title.value + " " + self.__names[-1]
            case self.NameFormats.CASUAL:  # E.g. John
                return self.__names[0]

    def set_name(self, new):  # Normal setter for names.
        if not (isinstance(new, list) and all(isinstance(item, str) for item in new)):
            return
        self.__names = new

    def set_title(self, new):  # Normal setter for title.
        if (not isinstance(new, Client.Titles)):
            return
        self.__title = new

    # Getter, setter for date of birth.
    def get_dob(self):
        return self.__dob

    def set_dob(self, new):
        if (not isinstance(new, datetime.date)):
            return
        self.__dob = new

    # Getter, setter for phone number.
    def get_phone(self):
        return self.__phone

    def set_phone(self, new):
        if (not isinstance(new, phonenumbers.PhoneNumber)):
            # Allow un-parsed inputs.
            self.set_phone(phonenumbers.parse("+1 {}".format(new)))
        self.__phone = new

    # Getter, setter for email.
    def get_email(self):
        return self.__email

    def set_email(self, new):
        if (not isinstance(new, str)):
            return
        self.__email = new

    # Getter, setter for address.
    def get_address(self):
        return self.__address

    def set_address(self, new):
        if (not isinstance(new, str)):
            return
        self.__address = new

    # Getter, setter for preferred branch.
    def get_preferred_branch(self):
        return self.__preferred_branch

    def set_preferred_branch(self, new):
        from branch import Branch  # Imported here to avoid circular reference.
        if (not isinstance(new, Branch)):
            return
        self.__preferred_branch = new

    # Getter, setter for preferred contact method.
    def get_preferred_contact_method(self):
        return self.__preferred_contact_method.value

    def set_preferred_contact_method(self, new):
        if (not isinstance(new, self.ContactMethods)):
            return
        self.__preferred_contact_method = new

    # Add and remove accounts from this user.
    def remove_account(self, acc):
        self.__accounts.remove(acc)

    def add_account(self, acc):
        # Imported here to avoid circular reference.
        from account import Account
        if not isinstance(acc, Account):
            return
        self.__accounts.append(acc)

    # Override built-in functions.
    def __str__(self):
        return ("ID_number=" + str(self.get_ID()) +
                ", name=\"" + self.printName(self.NameFormats.FULL) + "\""
                ", preferred_contact_method=" + self.get_preferred_contact_method())

    def __repr__(self):
        return ("ID_number=" + str(self.get_ID()) +
                ", name=\"" + self.printName(self.NameFormats.FULL) + "\""
                ", preferred_contact_method=" + self.get_preferred_contact_method())
