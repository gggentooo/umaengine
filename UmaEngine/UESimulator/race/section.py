"""
UESimulator.race.section

Section 오브젝트의 class definition
"""

from UESimulator.enums.raceattr import ESectionType, ESectionSlope

class Section:
    def __init__(self, length: int, type: ESectionType, slope: ESectionSlope):
        self._length: int = length
        self._type: ESectionType = type,
        self._slope: ESectionSlope = slope
        self._name: str = ""
    
    @property
    def length(self) -> int:
        return self._length
    @property
    def type(self) -> ESectionType:
        return self._type
    @property
    def slope(self) -> ESectionSlope:
        return self._slope
    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def setName(self, new_name: str):
        self._name = new_name
