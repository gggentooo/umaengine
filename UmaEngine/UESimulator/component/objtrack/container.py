"""
UESimulator.component.objtrack.container

시뮬레이션 중 모든 게임오브젝트를 메모리상 저장하는 wrapper class
"""

from UESimulator.uma.uma import Uma
from UESimulator.race.race import Race

class ObjContainer:
    def __init__(self):
        self._uma_arr: list[Uma] = list()
        self._race: Race
