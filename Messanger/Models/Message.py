from User import User
import ContentType


class Message:
    def __init__(self,body ,src:User ,dest:User, tcontent:ContentType = ContentType.TEXT):
        self.__body= body
        self.__tcontent = tcontent
        self.__src = src
        self.__dest = dest


    @property
    def Body (self):
        return self.__body

    @property
    def Tcontent(self):
        return self.__tcontent
    
    @property
    def Src(self):
        return self.__src

    @property
    def Dest (self):
        return self.__dest
