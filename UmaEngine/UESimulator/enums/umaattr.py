"""
UESimulator.enums.umaattr

우마 및 관련 클래스의 특성들을 enum의 형태로 저장
"""

from UESimulator.enums.base import UEIntEnum, UEStrEnum

# 스탯 (스피드, 스태미나, 파워, 근성, 지능)
class EStatType(UEStrEnum):
    SPEED = "스피드"
    STAMINA = "스태미나"
    POWER = "파워"
    TENACITY = "근성"
    INTELLIGENCE = "지능"

# 적성 단계 (G~S)
class ETalentLevel(UEIntEnum):
    G = 0
    F = 1
    E = 2
    D = 3
    C = 4
    B = 5
    A = 6
    S = 7

# 주법 (도주, 선행, 선입, 추입)
class EStrategy(UEStrEnum):
    NIGE = "도주"
    SENKOU = "선행"
    SASHI = "선입"
    OIKOMI = "추입"
