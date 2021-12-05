
class User:
    def __init__(self, name , password:str = ''):
        self.name = name
        self.password = password
        self.contacts = []