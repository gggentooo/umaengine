"""
UESimulator.component.base

컴포넌트 베이스 클래스 정의:
공통으로 쓰는 syslog와 race를 init에서 받아옴
"""

from UESimulator.component.systemlogger import SystemLogger
from UESimulator.race.race import Race
from UESimulator.uma.uma import Uma

class UEBaseComponent:
    def __init__(self, syslog: SystemLogger, race: Race, umalist: list[Uma]):
        self._syslog: SystemLogger = syslog
        self._race: Race = race
        self._umalist: list[Uma] = umalist
        
    @property
    def syslog(self):
        return self._syslog
    @property
    def race(self):
        return self._race
    @property
    def umalist(self):
        return self._umalist