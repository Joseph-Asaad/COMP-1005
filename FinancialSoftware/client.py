from abs_repr import AbsRepr
from hasUUID import hasUUID
import datetime
from phonenumbers import phonenumber
from account import Account
from branch import Branch

class Client(hasUUID):
    from enum import Enum

    def __init__(self, names, title, dob, phone, email, address, accounts, preferred_branch, preferred_contact_method=None):
        hasUUID.__init__(self)
        self.set_name(names)
        self.set_title(title)
        self.set_dob(dob)
        self.set_phone(phone)
        self.set_email(email)
        self.set_address(address)

        self.__accounts = []
        for acc in accounts : 
            self.add_account(acc)
            
        self.set_preferred_branch(preferred_branch)
        if preferred_contact_method == None : preferred_contact_method = self.ContactMethods.PHONE
        self.set_preferred_contact_method(preferred_contact_method)

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
            

    def set_name (self, new) : 
        if not (isinstance(new, list) and all(isinstance(item, str) for item in new)) : return
        self.__names = new

    def set_title (self, new) : 
        if (not isinstance(new, Client.Titles)) : return
        self.__title = new

    def get_dob (self) : 
        return self.__dob
    def set_dob (self, new) : 
        if (not isinstance(new, datetime.date)) : return
        self.__dob = new

    def get_dob (self) : 
        return self.__dob
    def set_dob (self, new) : 
        if (not isinstance(new, datetime.date)) : return
        self.__dob = new

    def get_phone (self) : 
        return self.__phone
    def set_phone (self, new) : 
        if (not isinstance(new, phonenumber.PhoneNumber)) : return
        self.__phone = new

    def get_email (self) : 
        return self.__email
    def set_email (self, new) : 
        if (not isinstance(new, str)) : return
        self.__email = new

    def get_address (self) : 
        return self.__address
    def set_address (self, new) : 
        if (not isinstance(new, str)) : return
        self.__address = new

    def get_preferred_branch (self) : 
        return self.__preferred_branch
    def set_preferred_branch (self, new) : 
        if (not isinstance(new, Branch)) : return
        self.__preferred_branch = new

    def get_preferred_contact_method (self) : 
        return self.__preferred_contact_method.value
    def set_preferred_contact_method (self, new) : 
        if (not isinstance(new, self.ContactMethods)) : return
        self.__preferred_contact_method = new

    def remove_account (self, acc) :
        self.__accounts.remove(acc)
    def add_account (self, acc) : 
        if not isinstance(acc, Account) : return
        self.__accounts.append(acc)

    def __str__(self):
        return ("ID_number=" + str(self.get_ID()) +
                ", name=\"" + self.printName(self.NameFormats.FULL) + "\""
                ", preferred_contact_method=" + self.get_preferred_contact_method())
