"""
UESimulator.race.section

Section 오브젝트의 class definition
"""

from UESimulator.enums.raceattr import ESectionType

class Section:
    def __init__(self, length: int, type: ESectionType):
        self._length = length
        self._type = type
