"""
UESimulator.uma.uma

Uma 오브젝트의 class definition
"""

from UESimulator.uma.stat import StatSet

class Uma:
    def __init__(self, id: int, name: str, stats: StatSet):
        self._id: int = id
        self._name: str = name
        self._stats: StatSet = stats
    
    @property
    def id(self):
        return self._id
    @property
    def name(self):
        return self._name
