"""
UESimulator.race.section

Section 오브젝트의 class definition
"""

from UESimulator.enums.raceattr import ESectionType, ESectionSlope

class Section:
    def __init__(self, name: str, length: int, type: ESectionType, slope: ESectionSlope):
        self._name: str = name
        self._length: int = length
        self._type: ESectionType = type
        self._slope: ESectionSlope = slope
        
    def __repr__(self):
        return f"{self.name} | {self.type} {self.length}m ({self.slope})"
    
    @property
    def name(self):
        return self._name
    @property
    def length(self):
        return self._length
    @property
    def type(self):
        return self._type
    @property
    def slope(self):
        return self._slope