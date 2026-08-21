from abs_repr import AbsRepr
from hasUUID import hasUUID

class Client(hasUUID, AbsRepr):
    from enum import Enum

    def __init__(self, ID_number, names, title, dob, phone, email, address, accounts, preferred_branch, preferred_contact_method=None):
        self.__names = names
        self.__title = title
        self.__dob = dob
        self.__phone = phone
        self.__email = email
        self.__address = address
        self.__accounts = accounts
        self.__preferred_branch = preferred_branch
        self.__preferred_contact_method = preferred_contact_method
        if self.preferred_contact_method == None:
            self.preferred_contact_method = self.ContactMethods.PHONE

    class Titles(Enum):
        MR = "Mr."
        MS = "Ms."
        MRS = "Mrs."
        DR = "Dr."
        SIR = "Sir"
        COLONEL = "Col."

    class ContactMethods(Enum):
        EMAIL = "email"
        PHONE = "phone"

    class NameFormats(Enum):
        DEFAULT = 0
        FULL = 1
        FORMAL = 2
        CASUAL = 3

    def printName(self, format):
        match format:
            case self.NameFormats.DEFAULT:
                return self.__names[0] + " " + self.__names[-1]
            case self.NameFormats.FULL:
                return ' '.join(self.__names)
            case self.NameFormats.FORMAL:
                return self.__title.value + " " + self.__names[-1]
            case self.NameFormats.CASUAL:
                return self.__names[0]

    

    def __str__(self):
        return ("ID_number=" + str(self.__ID_number) +
                ", name=\"" + self.printName(self.NameFormats.FULL) + "\""
                ", preferred_contact_method=" + self.preferred_contact_method.value)
