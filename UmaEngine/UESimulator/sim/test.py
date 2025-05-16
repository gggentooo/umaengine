"""
UESimulator - test.py

UmaEngine의 시뮬레이션 모듈 UESimulator 관련 테스트용 플레이그라운드 파일
"""

from UESimulator.sim.simulator import Simulator

class Test:
    def __init__(self):
        self._simulator = Simulator()
        
    @property
    def simulator(self):
        return self._simulator
