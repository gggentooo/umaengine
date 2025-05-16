"""
UESimulator.simulator

Simulator class definition
"""

from UESimulator.component.io.fileio import JsonReader

class Simulator:
    def __init__(self):
        self._jsonreader: JsonReader = JsonReader()
