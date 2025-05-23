"""
UESimulator.component.obj.load
"""

import UESimulator.component.err as UEerr
import UESimulator.enums.raceattr as RaceAttr
import UESimulator.enums.umaattr as UmaAttr
from UESimulator.component.base import UEBaseComponent
from UESimulator.component.fileio import JsonReader
from UESimulator.race.section import Section
from UESimulator.race.race import Race
from UESimulator.uma.stat import StatSet
from UESimulator.uma.uma import Uma

class ObjLoader(UEBaseComponent):
    def __init__(self, jsnrdr: JsonReader, *args):
        super().__init__(*args)
        self._jsnrdr = jsnrdr
    
    @property
    def jsnrdr(self):
        return self._jsnrdr
    
    def load_race(self, id: int) -> Race:
        try:
            r_dict = {e['meta']['id']: e for e in self.jsnrdr.read(self.jsnrdr.EFilePaths.RACE)}
            r_data = r_dict[id]
        except UEerr.FileNotFoundError: raise
        except KeyError: 
            raise UEerr.RaceNotFoundError
        
        try:
            rattr_name = str(r_data['meta']['name'])
            rattr_surf = RaceAttr.ERaceSurface(r_data['attr']['surface'])
            rattr_dir = RaceAttr.ERaceDirection(r_data['attr']['direction'])
            rattr_wthr = RaceAttr.ERaceWeather(r_data['attr']['weather'])
            rattr_fc = RaceAttr.ERaceFieldCondition(r_data['attr']['field_condition'])
            rattr_sections: list[Section] = []
            
            sec_raw = r_data['sections']
            stc = sum(RaceAttr.ESectionType(e['type']) == RaceAttr.ESectionType.STRETCH for e in sec_raw)
            cc = sum(RaceAttr.ESectionType(e['type']) == RaceAttr.ESectionType.CURB for e in sec_raw)
            st_idx = 0
            c_idx = 0
            for s in sec_raw:
                sattr_len = int(s['length'])
                sattr_type = RaceAttr.ESectionType(s['type'])
                sattr_slope = RaceAttr.ESectionSlope(s['slope'])
                sattr_name = ""
                if sattr_type == RaceAttr.ESectionType.STRETCH:
                    st_idx += 1
                    if st_idx < stc:
                        sattr_name = f"제 {st_idx} 직선"
                    else:
                        sattr_name = f"최종 직선"
                elif sattr_type == RaceAttr.ESectionType.CURB:
                    c_idx += 1
                    if c_idx < cc:
                        sattr_name = f"제 {c_idx} 코너"
                    else:
                        sattr_name = f"최종 코너"
                sec_obj = Section(sattr_name, sattr_len, sattr_type, sattr_slope)
                rattr_sections.append(sec_obj)
            
            ulist_raw = r_data['uma_list']
            u_idx = 0
            for u in ulist_raw:
                u_idx += 1
                try:
                    uma = self.load_uma(int(u['id']), UmaAttr.EStrategy(u['strategy']), u_idx)
                    self.umalist.append(uma)
                except (UEerr.UmaNotFoundError, UEerr.InvalidUmaDataError):
                    raise
            
            race = Race(
                rattr_name,
                rattr_surf,
                rattr_dir,
                rattr_wthr,
                rattr_fc,
                rattr_sections
            )
        except (KeyError, ValueError):
            raise UEerr.InvalidRaceDataError
        
        return race
    
    def load_uma(self, id: int, strategy: UmaAttr.EStrategy, gatenum: int) -> Uma:
        try:
            u_dict = {e['meta']['id']: e for e in self.jsnrdr.read(self.jsnrdr.EFilePaths.UMA)}
            u_data = u_dict[id]
        except UEerr.FileNotFoundError: raise
        except KeyError: 
            raise UEerr.UmaNotFoundError
        
        try:
            uattr_name = str(u_data['meta']['name'])
            uattr_stats = StatSet(
                int(u_data['stats']['speed']),
                int(u_data['stats']['stamina']),
                int(u_data['stats']['power']),
                int(u_data['stats']['tenacity']),
                int(u_data['stats']['intelligence'])
            )
            
            uma = Uma(
                gatenum,
                id,
                uattr_name,
                uattr_stats,
                strategy
            )
        except (KeyError, ValueError):
            raise UEerr.InvalidUmaDataError
        
        return uma
        