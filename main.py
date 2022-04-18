import datetime
from datetime import date
from datetime import timedelta
from collections import UserDict
from hashlib import new
now = datetime.datetime.now()

class Field:
    def __init__(self, value):
        self._value = value

    def __str__(self) -> str:
        return self._value

    def __repr__(self) -> str:
        return self._value


class Name(Field):
    pass

class Email(Field):
    pass

class Birthday(Field):
    @property
    def value(self):
        return self.value
    
    @value.setter
    def value(self, new_value):
        if 0 < new_value.day < 32 and 0 < new_value.month < 13 and 1900 < new_value.year < now.year:
            self.value = new_value
        else:
            raise ValueError('Wrond number')
        
class Phone(Field):
    @property
    def value(self):
        return self.value
    
    @value.setter
    def value(self, new_value):
        if 11 < len(str(new_value)) < 14:
            self.value = new_value
        else:
            raise ValueError('Wrond number')



class Record:
    def __init__(self, name, birthday: Birthday = None, phone: Phone = None, email: Email = None):
        self.name = name
        self.birthday = birthday
        self.email = email
        self.phones = []
        if phone:
            self.phones.append(phone)

    def add_new_number(self, phone: Phone):
        self.phones.append(phone)

    def delete_number(self, phone: Phone):
        self.phones.remove(phone)

    def change_number(self, phone: Phone, new_phone: Phone):
        self.phones.remove(phone)
        self.phones.append(new_phone)
        
    def days_to_birthday(self):
        if self.birthday == None:
            print("Birthday not specified")
        else:
            br = datetime.datetime(year = now.year, month = self.birthday._value.month, day = self.birthday._value.day)
            if (br - now).days > 0:
                return (br - now).days
            else:
                return 365 - (br - now).days
        

class AddressBook(UserDict):
    def add_new_contact(self, contact: Record):
        self.data[contact.name._value] = contact
    # я так и не понял как сделать iterator    
    def iterator(self, N):
        start = 0
        limit = N
        while True:
            yield "\n".join([self.data[self.name._value]])
            start, limit = start + N, limit + N
            if start >= len(self.data):
                break

if __name__ == "__main__":
    n1 = Name("Bill")
    p1 = Phone("12345678")
    p2 = Phone("98763566")
    k = datetime.datetime(2003, 9, 1)
    b1 = Birthday(k)
    rec1 = Record(n1)
    rec1.add_new_number(p1)
    rec1.add_new_number(p2)

    ab = AddressBook()
    ab.add_new_contact(rec1)

    print(ab["Bill"].phones)

    rec1.change_number(p1, Phone("098767"))

    print(ab["Bill"].phones)

    ab["Bill"].delete_number(p2)

    print(ab["Bill"].phones)
    print("1")
    ab.iterator(1)
    print("2")
    
    print(rec1.days_to_birthday())
