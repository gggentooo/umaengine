"""
UESimulator.enums.raceattr

레이스 및 구간의 특성들을 enum의 형태로 저장
"""

from UESimulator.enums.base import UEIntEnum, UEStrEnum

"""
레이스 특성
"""
# 회전 방향 (직선, 시계방향, 반시계방향)
class ERaceDirection(UEStrEnum):
    STRAIGHT = "직선"
    RIGHT = "우"
    LEFT = "좌"

# 거리 유형 (단거리, 마일, 중거리, 장거리)
class ERaceDistanceType(UEStrEnum):
    SPRINT = "단거리"
    MILE = "마일"
    MIDDLE = "중거리"
    LONG = "장거리"
# 거리 유형 기준
class ERaceDTThresholds(UEIntEnum):
    MILE = 1600
    MIDDLE = 1900
    LONG = 2500

# 마장 유형 (잔디, 더트)
class ERaceSurface(UEStrEnum):
    TURF = "잔디"
    DIRT = "더트"

# 날씨
class ERaceWeather(UEStrEnum):
    SUNNY = "맑음"
    CLOUDY = "흐림"
    RAINY = "비"
    SNOWY = "눈"
# 마장 상태
class ERaceFieldCondition(UEStrEnum):
    GOOD = "양호"
    FIRM = "다습"
    SOFT = "포화"
    HEAVY = "불량"

"""
구간 특성
"""
# 구간 유형 (정지, 직선, 코너)
class ESectionType(UEStrEnum):
    STRETCH = "직선"
    CURB = "코너"

# 경사도 (평지, 오르막, 내리막)
class ESectionSlope(UEStrEnum):
    FLAT = "평지"
    UP = "오르막"
    DOWN = "내리막"
