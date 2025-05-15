"""
UESimulator - enums/constants.py

시뮬레이션에 사용되는 상수들을 enum의 형태로 정의
모든 enum class의 이름은 {E + (descriptor)} 형태가 되어야 함
"""

from UES_enums.base import UEEnum, UEIntEnum

"""
마신 단위

기준값 (1마신) 수정 가이드라인:
    a)  반드시 가준값은 16의 배수로 설정
    b)  기준값이 16의 배수가 아닌 경우,
        나머지 값은 기준값 기반 연산을 삭제하고
        수동으로 정수 값을 설정
"""
class EDist(UEIntEnum):
    ONE_LENGTH = 16                 # 기준값 (1마신)
    HALF_LENGTH = ONE_LENGTH / 2    # 1마신 == 16 기준, 8
    NECK = HALF_LENGTH / 2          # 4
    HEAD = NECK / 2                 # 2
    NOSE = HEAD / 2                 # 1

"""
스탯 종류

스스파근지 01234
EStatType(0).name => 'SPEED'
"""
class EStatType(UEIntEnum):
    SPEED = 0
    STAMINA = 1
    POWER = 2
    TENACITY = 3
    INTELLIGENCE = 4
