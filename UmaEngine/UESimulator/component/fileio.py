"""
UESimulator.component.fileio

외부 파일에 read/write하는 컴포넌트
"""

import json, os

import UESimulator.component.err as UEerr
from UESimulator.enums.base import UEStrEnum
from UESimulator.component.base import UEBaseComponent

class JsonReader(UEBaseComponent):
    class EFilePaths(UEStrEnum):
        RACE = os.path.join(os.path.dirname(__file__), "../../data/race.json")
        UMA = os.path.join(os.path.dirname(__file__), "../../data/uma.json")
    
    def read(self, filepath: str):
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                return json.load(file)
        except IOError:
            raise UEerr.FileNotFoundError