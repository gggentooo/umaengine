"""
UESimulator.component.io.fileio

외부 파일에 read/write하는 컴포넌트
"""

import json

class JsonReader():
    def __init__(self):
        self._data = None
        self._hasData = False
    
    def read(self, filepath: str):
        with open(filepath, "r", encoding="utf-8") as file:
            self._data = json.load(file)
            if self._data != None:
                self._hasData = True
    
    def clear_data(self):
        self._data = None
