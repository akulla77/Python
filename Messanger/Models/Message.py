from User import User
import ContentType


class Message:
    def __init__(self,body ,src:User ,dest:User, tcontent:ContentType = ContentType.TEXT):
        self.body= body
        self.tcontent = tcontent
        self.src = src
        self.dest = dest


