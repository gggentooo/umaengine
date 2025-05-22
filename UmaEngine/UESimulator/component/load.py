"""
UESimulator.component.obj.load
"""

import json, os

import UESimulator.component.err as UEerr
from UESimulator.component.systemlogger import SystemLogger
from UESimulator.component.fileio import JsonReader
from UESimulator.race.race import Race

class ObjLoader():
    def __init__(self, syslog: SystemLogger, jsnrdr: JsonReader):
        self._syslog: SystemLogger = syslog
        self._jsnrdr: JsonReader = jsnrdr
    
    @property
    def syslog(self) -> SystemLogger:
        return self._syslog
    @property
    def jsnrdr(self) -> JsonReader:
        return self._jsnrdr
    
    def load_race(self, id: int) -> Race:
        try:
            r_dict = {e['meta']['id']: e for e in self.jsnrdr.read(self.jsnrdr.EFilePaths.RACE)}
        except UEerr.FileNotFoundError: raise
        
        try:
            r_data = r_dict[id]
            race = Race(
                r_data['meta']['name']
            )
        except BaseException: 
            raise UEerr.RaceNotFoundError
        
        return race