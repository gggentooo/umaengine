"""
UESimulator - obj/race.py

Race 오브젝트의 class definition
"""

import UESimulator.enums.raceattr as RaceAttr
from UESimulator.race.section import Section

class Race:
    def __init__(self, name: str, surface: RaceAttr.ERaceSurface, direction: RaceAttr.ERaceDirection, weather: RaceAttr.ERaceWeather, field_condition: RaceAttr.ERaceFieldCondition, sections: list[Section]):
        self._name: str = name
        self._surface: RaceAttr.ERaceSurface = surface
        self._direction: RaceAttr.ERaceDirection = direction
        self._weather: RaceAttr.ERaceWeather = weather
        self._field_condition: RaceAttr.ERaceFieldCondition = field_condition
        self._sections: list[Section] = sections
        
        self._length: int = sum(s.length for s in self.sections)
        self._disttype: RaceAttr.ERaceDistanceType = RaceAttr.ERaceDistanceType.SPRINT
        if self.length >= RaceAttr.ERaceDTThresholds.MILE:
            self._disttype = RaceAttr.ERaceDistanceType.MILE
        if self.length >= RaceAttr.ERaceDTThresholds.MIDDLE:
            self._disttype = RaceAttr.ERaceDistanceType.MIDDLE
        if self.length >= RaceAttr.ERaceDTThresholds.LONG:
            self._disttype = RaceAttr.ERaceDistanceType.LONG
        
    def __repr__(self):
        return f"[{self.name}] | {self.surface} {self._length}m({self.disttype}) {self.direction} {self.weather} {self.field_condition}"
    
    @property
    def name(self):
        return self._name
    @property
    def surface(self):
        return self._surface
    @property
    def direction(self):
        return self._direction
    @property
    def weather(self):
        return self._weather
    @property
    def field_condition(self):
        return self._field_condition
    @property
    def sections(self):
        return self._sections
    @property
    def length(self):
        return self._length
    @property
    def disttype(self):
        return self._disttype