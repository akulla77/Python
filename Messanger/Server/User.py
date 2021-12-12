
class User:
    def __init__(self, name ):
        self.__name = name
        self.__contacts = []

    @property
    def Name (self):
        return self.__name
        
    @property
    def Contacts(self):
        return self.__contacts
    

