
from typing import Dict,Any
from  dataclasses import dataclass

@dataclass
class MesD:
    text:str
    src:str
    dest:str

    def to_json(self) -> Dict[str, Any]:
            return {
                'text': self.text,
                'src': self.src,
                'dest': self.dest
            }