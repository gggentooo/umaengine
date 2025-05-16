"""
UESimulator - test.py

UmaEngine의 시뮬레이션 모듈 UESimulator 관련 테스트용 플레이그라운드 파일
"""

from UESimulator.enums.constants import EDist
from UESimulator.enums.umaattr import EStatType
from UESimulator.uma.stat import Stat, MutableStat, StatSet
from UESimulator.uma.uma import Uma

class Test:
    def sampleUmaInit(self) -> Uma:
        sset = StatSet(8, 7, 10, 5, 4)
        u = Uma(sset)
        return u

    def runTest(self):
        new_uma = self.sampleUmaInit()
        print(new_uma.speed)

    
