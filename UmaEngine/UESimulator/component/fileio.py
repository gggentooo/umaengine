"""
UESimulator.component.fileio

외부 파일에 read/write하는 컴포넌트
"""

import json, os

import UESimulator.component.err as UEerr
from UESimulator.component.systemlogger import SystemLogger
from UESimulator.enums.base import UEStrEnum

class JsonReader():
    def __init__(self, syslog: SystemLogger):
        self._data = None
        self._syslog: SystemLogger = syslog
        
    class EFilePaths(UEStrEnum):
        RACE = os.path.join(os.path.dirname(__file__), "../../data/race.json")
        UMA = os.path.join(os.path.dirname(__file__), "../../data/uma.json")
        
    @property
    def syslog(self) -> SystemLogger:
        return self._syslog
    
    def read(self, filepath: EFilePaths):
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                self._data = json.load(file)
        except IOError:
            raise UEerr.FileNotFoundError

        return self._data