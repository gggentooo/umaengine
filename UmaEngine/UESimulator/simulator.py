"""
UESimulator.simulator

Simulator class definition
"""

import UESimulator.component.err as err
from UESimulator.component.fileio import JsonReader
from UESimulator.component.gamelogger import GameLogger
from UESimulator.component.load import ObjLoader
from UESimulator.component.systemlogger import SystemLogger
from UESimulator.race.race import Race
from UESimulator.uma.uma import Uma

class Simulator:
    def __init__(self):
        self._race: Race = None
        self._umalist: list[Uma] = []
        self._syslog: SystemLogger = SystemLogger()
        self._gamlog: GameLogger = GameLogger(self.syslog, self.race, self.umalist)
        self._jsnrdr: JsonReader = JsonReader(self.syslog, self.race, self.umalist)
        self._objldr: ObjLoader = ObjLoader(self.jsnrdr, self.syslog, self.race, self.umalist)

    @property
    def race(self):
        return self._race
    @property
    def umalist(self):
        return self._umalist
    @property
    def syslog(self):
        return self._syslog
    @property
    def gamlog(self):
        return self._gamlog
    @property
    def jsnrdr(self):
        return self._jsnrdr
    @property
    def objldr(self):
        return self._objldr
    
    def initialize(self):
        try:
            race_id = int(self.syslog.prompt("레이스 ID를 입력해 주세요"))
            self._race = self.objldr.load_race(race_id)
        except err.UEError as e:
            self.syslog.log(-1, e.message)
            raise err.SimulationInitFailError
        
        self.syslog.log(0, f"레이스 로드 완료:\n{self.race}")
        self.syslog.log(0, f"출전자 로드 완료:\n{'\n'.join(str(u) for u in self.umalist)}")
        
    def simulate(self):
        try:
            self.initialize()
        except err.UEError as e:
            self.syslog.log(-1, e.message)