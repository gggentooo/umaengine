"""
UESimulator - obj/uma.py

Uma 오브젝트의 class definition
"""

from UES_obj.stat import StatSet

class Uma:
    def __init__(self, stats: StatSet):
        self._stats = stats
    
    # 스탯 read
    @property
    def speed(self) -> int:
        return self._stats._speed.value
    @property
    def stamina(self) -> int:
        return self._stats._stamina.value
    @property
    def power(self) -> int:
        return self._stats._power.value
    @property
    def tenacity(self) -> int:
        return self._stats._tenacity.value
    @property
    def intelligence(self) -> int:
        return self._stats._intelligence.value
