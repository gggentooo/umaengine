"""
UESimulator.simulator

Simulator class definition
"""

import UESimulator.component.err as err
from UESimulator.component.systemlogger import SystemLogger
from UESimulator.component.fileio import JsonReader
from UESimulator.component.load import ObjLoader
from UESimulator.race.race import Race

class Simulator:
    def __init__(self):
        self._syslog: SystemLogger = SystemLogger()
        self._jsnrdr: JsonReader = JsonReader(self.syslog)
        self._objldr: ObjLoader = ObjLoader(self.syslog, self.jsnrdr)
        self._race: Race = None
        
    @property
    def syslog(self) -> SystemLogger:
        return self._syslog
    @property
    def jsnrdr(self) -> JsonReader:
        return self._jsnrdr
    @property
    def objldr(self) -> ObjLoader:
        return self._objldr
    @property
    def race(self):
        return self._race
    
    def initialize(self):
        try:
            race_id = int(self.syslog.prompt("레이스 ID를 입력해 주세요."))
        except err.UEError as e:
            self.syslog.log(-1, e.message)
            raise err.SimulationInitFailError
        else:
            try:
                self._race = self.objldr.load_race(race_id)
            except err.UEError as e:
                self.syslog.log(-1, e.message)
                raise err.SimulationInitFailError
        
        print(self.race.name)
        
    def simulate(self):
        try:
            self.initialize()
        except err.UEError as e:
            self.syslog.log(-1, e.message)