"""
UESimulator.enums.raceattr

레이스 및 구간의 특성들을 enum의 형태로 저장
"""

from UESimulator.enums.base import UEIntEnum

"""
레이스 특성
"""
# 회전 방향 (직선, 시계방향, 반시계방향)
class ERaceDirection(UEIntEnum):
    STRAIGHT = 0        # 직선
    RIGHT = 1           # 시계방향 (우)
    LEFT = 2            # 반시계방향 (좌)

# 거리 유형 (단거리, 마일, 중거리, 장거리)
class ERaceDistanceType(UEIntEnum):
    SPRINT = 0          # 단거리
    MILE = 1            # 마일
    CLASSIC = 2         # 중거리
    LONG = 3            # 장거리

# 마장 유형 (잔디, 더트)
class ERaceSurface(UEIntEnum):
    TURF = 0            # 잔디
    DIRT = 1            # 더트

"""
구간 특성
"""
# 구간 유형 (직선, 코너)
class ESectionType(UEIntEnum):
    STRETCH = 0         # 직선
    CURB = 1            # 코너

# 경사도 (평지, 오르막, 내리막)
class ESectionSlope(UEIntEnum):
    FLAT = 0            # 평지
    UP = 1              # 오르막
    DOWN = 2            # 내리막
