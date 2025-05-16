"""
UESimulator.enums.raceattr

우마 및 관련 클래스의 특성들을 enum의 형태로 저장
"""

from UESimulator.enums.base import UEIntEnum

# 스탯 (스피드, 스태미나, 파워, 근성, 지능)
class EStatType(UEIntEnum):
    SPEED = 0           # 스피드
    STAMINA = 1         # 스태미나
    POWER = 2           # 파워
    TENACITY = 3        # 근성
    INTELLIGENCE = 4    # 지능

# 주법 (도주, 선행, 선입, 추입)
class EStrategy(UEIntEnum):
    NIGE = 0            # 도주
    SENKOU = 1          # 선행
    SASHI = 2           # 선입
    OIKOMI = 3          # 추입
