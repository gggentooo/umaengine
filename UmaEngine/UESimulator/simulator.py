"""
UESimulator.simulator

Simulator class definition
"""

from UESimulator.component.fileio import JsonReader

class Simulator:
    def __init__(self):
        self._jsonreader: JsonReader = JsonReader()
    
    def simulate(self):
        pass