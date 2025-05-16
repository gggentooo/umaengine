"""
UESimulator - obj/simulator.py

Simulator 오브젝트의 class definition
"""

from UESimulator.component.objtrack.container import ObjContainer

class Simulator:
    def __init__(self):
        self._obj_container: ObjContainer = ObjContainer()
