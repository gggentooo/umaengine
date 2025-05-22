"""
UESimulator - obj/race.py

Race 오브젝트의 class definition
"""

class Race:
    def __init__(self, name: str):
        self._name: str = name
        
    @property
    def name(self):
        return self._name
