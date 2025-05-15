"""
UESimulator - obj/stat.py

Class definitions for:
class Stat
class MutableStat(Stat)
"""

from UES_enums.constants import EStatType

"""
기본 Stat 클래스
"""
class Stat:
    def __init__(self, type: EStatType, value: int):
        self._type: EStatType = type
        self._value: int = value
        
    @property
    def type(self) -> EStatType:
        return self._type
    
    @property
    def value(self) -> int:
        return self._value

"""
_value의 수정이 가능한 Stat
"""
class MutableStat(Stat):
    @Stat.value.setter
    def value(self, new_value):
        self._value = new_value

"""
스스파근지 세트
"""
class StatSet:
    def __init__(self, speed: int, stamina: int, power: int, tenacity: int, intelligence: int):
        self._speed: Stat = Stat(EStatType.SPEED, speed)
        self._stamina: Stat = Stat(EStatType.STAMINA, stamina)
        self._power: Stat = Stat(EStatType.POWER, power)
        self._tenacity: Stat = Stat(EStatType.TENACITY, tenacity)
        self._intelligence: Stat = Stat(EStatType.INTELLIGENCE, intelligence)
