
class BusinessCard:
    def set_info(self, name, email, addr):
        self.name = name
        self.email = email
        self.addr = addr


    def print_info(self):
        print("---------------------------")
        print("Name: ", self.name)
        print("E-mail: ", self.email)
        print("Address: ", self.addr)
        print("---------------------------")


class Myclass:
    def __init__(self, name, email, addr):
        self.name = name
        self.email = email
        self.addr = addr


    def print_info(self):
        print("---------------------------")
        print("Name: ", self.name)
        print("E-mail: ", self.email)
        print("Address: ", self.addr)
        print("---------------------------")
