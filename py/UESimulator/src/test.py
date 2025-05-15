"""
UESimulator - test.py

UmaEngine의 시뮬레이션 모듈 UESimulator 관련 테스트용 플레이그라운드 파일
"""

from UES_enums.constants import EDist, EStatType
from UES_obj.stat import Stat, MutableStat, StatSet
from UES_obj.uma import Uma

def sampleUmaInit() -> Uma:
    sset = StatSet(8, 7, 10, 5, 4)
    u = Uma(sset)
    return u

def main():
    new_uma = sampleUmaInit()
    print(new_uma.speed)
    new_uma.speed = 10
    print(new_uma.speed)
    
if __name__ == "__main__":
    main()
