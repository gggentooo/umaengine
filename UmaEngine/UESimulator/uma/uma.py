"""
UESimulator.uma.uma

Uma 오브젝트의 class definition
"""

import UESimulator.enums.umaattr as UmaAttr
from UESimulator.uma.stat import StatSet

class Uma:
    def __init__(self, gatenum: int, id: int, name: str, stats: StatSet, strategy: UmaAttr.EStrategy):
        self._gatenum: int = gatenum
        self._id: int = id
        self._name: str = name
        self._stats: StatSet = stats
        self._strategy: UmaAttr.EStrategy = strategy
    
    def __repr__(self):
        return f"[{self.gatenum}]{self.name}({self.strategy})"
    
    @property
    def gatenum(self):
        return self._gatenum
    @property
    def id(self):
        return self._id
    @property
    def name(self):
        return self._name
    @property
    def stats(self):
        return self._stats
    @property
    def strategy(self):
        return self._strategy