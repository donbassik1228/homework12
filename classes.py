# from datetime import datetime
# from collections import UserDict

# class Field:
#     def __init__(self, value):
#         if not self.is_valid(value):
#             raise ValueError("Invalid value")
#         self.__value = value

#     def __str__(self):
#         return str(self.__value)

#     def is_valid(self, value):
#         return True

#     @property
#     def value(self):
#         return self.__value

#     @value.setter
#     def value(self, value):
#         if not self.is_valid(value):
#             raise ValueError("Invalid value")
#         self.__value = value

# class Name(Field):
#     pass

# class Phone(Field):
#     @staticmethod
#     def is_valid(phone_number):
#         return len(phone_number) == 10 and phone_number.isdigit()

# class Birthday(Field):
#     @staticmethod
#     def is_valid(value):
#         try:
#             datetime.strptime(value, '%Y-%m-%d')
#         except ValueError:
#             return False
#         return True

#     def days_to_birthday(self):
#         today = datetime.now()
#         birthday = datetime.strptime(self.value, '%Y-%m-%d')
#         next_birthday = datetime(today.year, birthday.month, birthday.day)

#         if today > next_birthday:
#             next_birthday = datetime(today.year + 1, birthday.month, birthday.day)

#         days_left = (next_birthday - today).days
#         return days_left

# class Record:
#     def __init__(self, name, phone_number=None, birthday=None):
#         self.name = Name(name)
#         self.phones = []
#         if phone_number:
#             self.phones.append(Phone(phone_number))
#         self.birthday = Birthday(birthday) if birthday else None

#     def add_phone(self, phone_number):
#         phone = Phone(phone_number)
#         self.phones.append(phone)

#     def remove_phone(self, phone_number):
#         self.phones = [phone for phone in self.phones if phone.value != phone_number]

#     def find_phone(self, phone_number):
#         for phone in self.phones:
#             if phone.value == phone_number:
#                 return phone
#         return None

#     def edit_phone(self, old_phone_number, new_phone_number):
#         if not Phone.is_valid(new_phone_number):
#             raise ValueError("Invalid phone number")

#         found = False
#         for phone in self.phones:
#             if phone.value == old_phone_number:
#                 if not Phone.is_valid(old_phone_number):
#                     raise ValueError("Invalid old phone number")

#                 phone.value = new_phone_number
#                 found = True
#                 break
#         if not found:
#             raise ValueError("Phone number not found")

#     def days_to_birthday(self):
#         if self.birthday:
#             return self.birthday.days_to_birthday()
#         return None

#     def __str__(self):
#         phones_str = '; '.join(str(phone) for phone in self.phones)
#         return f"Contact name: {self.name.value}, phones: {phones_str}, birthday: {self.birthday}"

# class AddressBook(UserDict):
#     def __iter__(self, page_size=5):
#         current_page = 0
#         total_records = len(self.data)
#         while current_page * page_size < total_records:
#             yield list(self.data.values())[current_page * page_size: (current_page + 1) * page_size]
#             current_page += 1

#     def add_record(self, record):
#         if record.name.value in self.data:
#             return self.data[record.name.value] 
#         self.data[record.name.value] = record
#         return record 
    


#     def find(self, name):
#         return self.data.get(name)

#     def delete(self, name):
#         if name in self.data:
#             del self.data[name]
#     def __str__(self) -> str:
#         return "\n".join(str(r) for r in self.data.values())
# book = AddressBook()

# john_record = Record("John", phone_numbers=["1234567890", "5555555555"], birthday="1990-01-15")
# book.add_record(john_record)

# jane_record = Record("Jane", phone_numbers=["9876543210"], birthday="1985-05-20")
# book.add_record(jane_record)

# for page_number, page_records in enumerate(book):
#     print(f"Page {page_number + 1}:")
#     for record in page_records:
#         print(record)
#     print("\n")

# john = book.find("John")
# john.edit_phone("1234567890", "1112223333")

# print(john)

# try:
#     found_phone = john.find_phone("5555555555")
#     print(f"{john.name.value}: {found_phone}")
# except ValueError as e:
#     print(e)

# try:
#     john.edit_phone("1111111111", "9999999999")
# except ValueError as e:
#     print(e)

# book.delete("Jane")

from datetime import datetime
from collections import UserDict
from itertools import islice

class Field(UserDict):
    def __init__(self, value):
        if not self.is_valid(value):
            raise ValueError("Invalid value")
        self.__value = value

    def __str__(self):
        return str(self.__value)

    def is_valid(self, value):
        return True

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if not self.is_valid(value):
            raise ValueError("Invalid value")
        self.__value = value

class Name(Field):
    pass

class Phone(Field):
    @staticmethod
    def is_valid(phone_number):
        return len(phone_number) == 10 and phone_number.isdigit()

class Birthday(Field):
    @staticmethod
    def is_valid(value):
        try:
            datetime.strptime(value, '%Y-%m-%d')
        except ValueError:
            return False
        return True

    def days_to_birthday(self):
        today = datetime.now()
        birthday = datetime.strptime(self.value, '%Y-%m-%d')
        next_birthday = datetime(today.year, birthday.month, birthday.day)

        if today > next_birthday:
            next_birthday = datetime(today.year + 1, birthday.month, birthday.day)

        days_left = (next_birthday - today).days
        return days_left

class Record:
    def __init__(self, name, phone_number=None, birthday=None):
        self.name = Name(name)
        self.phones = []
        if phone_number:
            self.phones.append(Phone(phone_number))
        self.birthday = Birthday(birthday) if birthday else None

    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        self.phones.append(phone)

    def remove_phone(self, phone_number):
        self.phones = [phone for phone in self.phones if phone.value != phone_number]

    def edit_phone(self, old_phone_number, new_phone_number):
        if not Phone.is_valid(new_phone_number):
            raise ValueError("Invalid phone number")

        found = False
        for phone in self.phones:
            if phone.value == old_phone_number:
                if not Phone.is_valid(old_phone_number):
                    raise ValueError("Invalid old phone number")

                phone.value = new_phone_number
                found = True
                break
        if not found:
            raise ValueError("Phone number not found")

    def days_to_birthday(self):
        if self.birthday:
            return self.birthday.days_to_birthday()
        return None

    def __str__(self):
        phones_str = '; '.join(str(phone) for phone in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}, birthday: {self.birthday}"

class AddressBook(UserDict):
    def __iter__(self, page_size=5):
        total_records = len(self.data)
        for i in range(0, total_records, page_size):
            yield list(islice(self.data.values(), i, i + page_size))

    def add_record(self, record):
        if record.name.value in self.data:
            raise ValueError("Record with the same name already exists")
        self.data[record.name.value] = record
        return record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def __str__(self):
        return "\n".join(str(r) for r in self.data.values())









