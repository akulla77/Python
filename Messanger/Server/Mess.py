
from typing import Dict,Any
from  dataclasses import dataclass

@dataclass
class Mess:
    def __init__(self,text ,src ,dest,time):
        self.__text= text
        self.__src = src
        self.__dest = dest
        self.__time= time

    def to_json(self) -> Dict[str, Any]:
            return {
                'text': str(self.__text),
                'src': str(self.__src),
                'dest': str(self.__dest),
                'time': str(self.__time)
            }


    @property
    def Text (self):
        return self.__text
    
    @property
    def Src(self):
        return self.__src

    @property
    def Dest (self):
        return self.__dest
    
    @property
    def Time (self):
        return self.__time
