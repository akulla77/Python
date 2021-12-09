
class User:
    def __init__(self, name , password:str = ''):
        self.__name = name
        self.__password = password
        self.__contacts = []

    @property
    def Name (self):
        return self.__name

    @property
    def Password(self):
        return self.__password
    
    @property
    def Contacts(self):
        return self.__contacts
    

