# from classes import AddressBook, Record
# import pickle


# class Bot:

#     def __init__(self):
#         self.file = 'contacts.json'
#         self.book = AddressBook()
#         try:
#             with open(self.file, 'rb') as f:
#                 contacts = pickle.load(f)
#                 self.book.data = contacts
#         except:
#             print("Created new AdressBook")



#     @staticmethod

#     def input_error(func):
#         def wrapper(*args, **kwargs):
#             try:
#                 return func(*args, **kwargs)
#             except KeyError:
#                 return "Enter a user name"
#             except ValueError as e:
#                 if str(e) == "Contact already exists. Use 'change' command to update the phone number.":
#                     return "Contact already exists. Use 'change' command to update the phone number."
#                 return "Provide both name and phone, please"
#             except IndexError:
#                 return "Invalid command format"
#         return wrapper

#     @input_error
#     def add_contact(self, command):
#         name, phone = command.replace("add", "", 0).split()
#         # if name is not exsisting
#         record = Record(name, phone)

#         self.book.add_record(record)
#         # if name is  exsisting
#         # ..........

#         return f"Contact {name} added successfully"
#     def show_all_contacts(self, command):
#         if not self.book.data:
#             return "No contacts available"
        
#         return self.book
        

#     @input_error
#     def change_phone(self, command):
#         name, phone = command.replace('change ', "", 0).split()
#         if name not in self.book.data:
#             raise ValueError(f"Contact '{name}' does not exist. Use 'add' command to add a new contact.")
        
#         # contacts[name] = phone
#         return f"Phone number for {name} updated successfully"

#     @input_error
#     def get_phone(self, command):
#         name = command.replace('phone ', "", 0)
#         # if name not in contacts:
#         #     raise KeyError
#         # return f"The phone number for {name} is {contacts[name]}"

#     # def show_all_contacts(self, command):
#     #     if not contacts:
#     #         return "No contacts available"
#     #     result = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
#     #     return result

#     def bye(self, command):
#         with open(self.file, 'wb') as f:
#             pickle.dump(self.book.data, f)
#         return "Good bye!"
    

#     def search(self, command):
#         text = command.replace('search ', "", 0)
#         searched_text = text.strip().lower()
#         result = []
#         if not searched_text:
#             return result
#         for record in self.book.data.values():
#             if searched_text in record.name.value.lower() + ' '.join([phone.value for phone in record.phones]):
#                 result.append(record)
#         return result


#     def hello(self, command):
#         return "How can I help you?"
#     @input_error
#     def bad_command(self,command):
#         return "Invalid command. Please try again"

#     ACTIONS = {
#         "hello": hello,
#         "add": add_contact,
#         "change": change_phone, 
#         "phone": get_phone,
#         "search": search,
#         "show all": show_all_contacts,
#         "good bye": bye,
#         "exit": bye, 
#         "close": bye
#     }
#     @input_error
#     def get_handler(self, user_input):
#         for action in self.ACTIONS:
#             if user_input.startswith(action):
#                 return self.ACTIONS[action]
#         return self.bad_command
#     def run(self):
#         while True:
#             command = input("Enter a command: ").lower()
#             handler = self.get_handler(command)
#             result = handler(self, command)
#             print(result)
#             # check command to close bot 
#             if result == 'Good bye!':
#                 break

#             '''
#             if command == "hello":
#                 print("How can I help you?")
#             elif command.startswith("add "):
#                 try:
#                     _, name, phone = command.split(maxsplit=2)
#                     response = self.add_contact(name, phone)
#                 except ValueError as e:
#                     response = str(e)
#                 print(response)
#             elif command.startswith("change"):
#                 try:
#                     _, name, phone = command.split(maxsplit=2)
#                     response = change_phone(name, phone)
#                 except ValueError as e:
#                     response = str(e)
#                 print(response)
#             elif command.startswith("phone"):
#                 try:
#                     _, name = command.split(maxsplit=1)
#                     response = get_phone(name)
#                 except ValueError as e:
#                     response = str(e)
#                 print(response)
#             elif command == "show all":
#                 print(show_all_contacts())
#             elif command in ["good bye", "close", "exit"]:
#                 answer = self.bye()
#                 print(answer)
#                 break
#             else:
#                 print("Invalid command. Please try again")
# '''


from classes import AddressBook, Record
import pickle


class Bot:

    def __init__(self):
        self.file = 'contacts.json'
        self.book = AddressBook()
        try:
            with open(self.file, 'rb') as f:
                contacts = pickle.load(f)
                self.book.data = contacts
        except FileNotFoundError:
            print("Created a new AddressBook")

    @staticmethod
    def input_error(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except KeyError:
                return "Enter a user name"
            except ValueError as e:
                if str(e) == "Contact already exists. Use 'change' command to update the phone number.":
                    return "Contact already exists. Use 'change' command to update the phone number."
                return "Provide both name and phone, please"
            except IndexError:
                return "Invalid command format"
        return wrapper

    @input_error
    def add_contact(self, command):
        name, phone = command.replace("add ", " ").split()
        record = Record(name, phone)
        self.book.add_record(record)
        return f"Contact {name} added successfully"

    def show_all_contacts(self, command):
        if not self.book.data:
            return "No contacts available"
        return str(self.book)

    @input_error
    def change_phone(self, command):
        name, phone = command.replace('change ', "").split()
        if name not in self.book.data:
            raise ValueError(f"Contact '{name}' does not exist. Use 'add' command to add a new contact.")
        
        # self.book.data[name] = phone
        return f"Phone number for {name} updated successfully"

    @input_error
    def get_phone(self, command):
        name = command.replace('phone ', "")
        # if name not in self.book.data:
        #     raise KeyError
        # return f"The phone number for {name} is {self.book.data[name]}"

    def bye(self, command):
        with open(self.file, 'wb') as f:
            pickle.dump(self.book.data, f)
        return "Goodbye!"

    def search(self, command):
        text = command.replace('search ', "")
        searched_text = text.strip().lower()
        result = []
        if not searched_text:
            return result
        for record in self.book.data.values():
            if searched_text in record.name.value.lower() + ' '.join([phone.value for phone in record.phones]):
                result.append(record)
        return result

    def hello(self, command):
        return "How can I help you?"

    @input_error
    def bad_command(self, command):
        return "Invalid command. Please try again"

    ACTIONS = {
        "hello": hello,
        "add": add_contact,
        "change": change_phone,
        "phone": get_phone,
        "search": search,
        "show all": show_all_contacts,
        "goodbye": bye,
        "exit": bye,
        "close": bye
    }

    @input_error
    def get_handler(self, user_input):
        for action, handler in self.ACTIONS.items():
            if user_input.startswith(action):
                return handler
        return self.bad_command

    def run(self):
        while True:
            command = input("Enter a command: ").lower()
            handler = self.get_handler(command)
            result = handler(self, command)
            print(result)
            if result == 'Goodbye!':
                break